from design_baselines.data import StaticGraphTask
from design_baselines.logger import Logger
from design_baselines.mins.trainers import Ensemble
from design_baselines.mins.trainers import WeightedGAN
from design_baselines.mins.nets import ForwardModel
from design_baselines.mins.nets import Discriminator, DiscriminatorConv
from design_baselines.mins.nets import DiscreteGenerator, DiscreteGenConv
from design_baselines.mins.nets import ContinuousGenerator, ContinuousGenConv
from design_baselines.mins.utils import get_weights
from design_baselines.mins.utils import get_synthetic_data
import tensorflow as tf
import os


def model_inversion(config):
    """Optimize a design problem score using the algorithm MINS
    otherwise known as Model Inversion Networks

    Args:

    config: dict
        a dictionary of hyper parameters such as the learning rate
    """

    # create the training task and logger
    logger = Logger(config['logging_dir'])
    task = StaticGraphTask(config['task'], **config['task_kwargs'])
    base_temp = config.get('base_temp', None)

    if config['fully_offline']:

        # make several keras neural networks with two hidden layers
        forward_models = [ForwardModel(
            task.input_shape,
            hidden=config['hidden_size'],
            initial_max_std=config['initial_max_std'],
            initial_min_std=config['initial_min_std'])
            for b in range(config['bootstraps'])]

        # create a trainer for a forward model with a conservative objective
        ensemble = Ensemble(forward_models,
                            forward_model_optim=tf.keras.optimizers.Adam,
                            forward_model_lr=config['ensemble_lr'],
                            is_discrete=config['is_discrete'],
                            noise_std=config.get('noise_std', 0.0),
                            keep=config.get('keep', 1.0),
                            temp=config.get('temp', 0.001))

        # create a manager for saving algorithms state to the disk
        ensemble_manager = tf.train.CheckpointManager(
            tf.train.Checkpoint(**ensemble.get_saveables()),
            os.path.join(config['logging_dir'], 'ensemble'), 1)

        # build a bootstrapped data set
        train_data, val_data = task.build(
            bootstraps=config['bootstraps'],
            batch_size=config['ensemble_batch_size'],
            val_size=config['val_size'])

        # train the model for an additional number of epochs
        ensemble_manager.restore_or_initialize()
        ensemble.launch(train_data,
                        val_data,
                        logger,
                        config['ensemble_epochs'])

    if config['is_discrete'] and config['is_conv']:

        # build a Gumbel-Softmax GAN to sample discrete outputs
        explore_gen = DiscreteGenConv(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])
        exploit_gen = DiscreteGenConv(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])

    elif config['is_discrete']:

        # build a Gumbel-Softmax GAN to sample discrete outputs
        explore_gen = DiscreteGenerator(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])
        exploit_gen = DiscreteGenerator(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])

    elif config['is_conv']:

        # build an LS-GAN to sample continuous outputs
        explore_gen = ContinuousGenConv(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])
        exploit_gen = ContinuousGenConv(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])

    else:

        # build an LS-GAN to sample continuous outputs
        explore_gen = ContinuousGenerator(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])
        exploit_gen = ContinuousGenerator(
            task.input_shape, config['latent_size'],
            hidden=config['hidden_size'])

    # choose if the discriminator is convolutional or not
    discrimimator = DiscriminatorConv \
        if config['is_conv'] else Discriminator

    # build the neural network GAN components
    explore_discriminator = discrimimator(
        task.input_shape, hidden=config['hidden_size'])
    explore_gan = WeightedGAN(
        explore_gen, explore_discriminator,
        generator_lr=config['generator_lr'],
        generator_beta_1=config['generator_beta_1'],
        generator_beta_2=config['generator_beta_2'],
        discriminator_lr=config['discriminator_lr'],
        discriminator_beta_1=config['discriminator_beta_1'],
        discriminator_beta_2=config['discriminator_beta_2'],
        is_discrete=config['is_discrete'],
        noise_std=config.get('noise_std', 0.0),
        keep=config.get('keep', 1.0),
        start_temp=config.get('start_temp', 5.0),
        final_temp=config.get('final_temp', 1.0))

    # create a manager for saving algorithms state to the disk
    explore_gan_manager = tf.train.CheckpointManager(
        tf.train.Checkpoint(**explore_gan.get_saveables()),
        os.path.join(config['logging_dir'], 'exploration_gan'), 1)

    # build the neural network GAN components
    exploit_discriminator = discrimimator(
        task.input_shape, hidden=config['hidden_size'])
    exploit_gan = WeightedGAN(
        exploit_gen, exploit_discriminator,
        generator_lr=config['generator_lr'],
        generator_beta_1=config['generator_beta_1'],
        generator_beta_2=config['generator_beta_2'],
        discriminator_lr=config['discriminator_lr'],
        discriminator_beta_1=config['discriminator_beta_1'],
        discriminator_beta_2=config['discriminator_beta_2'],
        is_discrete=config['is_discrete'],
        noise_std=config.get('noise_std', 0.0),
        keep=config.get('keep', 1.0),
        start_temp=config.get('start_temp', 5.0),
        final_temp=config.get('final_temp', 1.0))

    # create a manager for saving algorithms state to the disk
    exploit_gan_manager = tf.train.CheckpointManager(
        tf.train.Checkpoint(**exploit_gan.get_saveables()),
        os.path.join(config['logging_dir'], 'exploitation_gan'), 1)

    # restore tha GANS if a checkpoint exists
    explore_gan_manager.restore_or_initialize()
    exploit_gan_manager.restore_or_initialize()

    # save the initial dataset statistics for safe keeping
    x = task.x
    y = task.y

    # build a weighted data set using newly collected samples
    train_data, val_data = task.build(
        x=x, y=y, importance_weights=get_weights(y, base_temp=base_temp),
        batch_size=config['gan_batch_size'],
        val_size=config['val_size'])

    # train the gan for several epochs
    explore_gan.launch(
        train_data, val_data, logger, config['initial_epochs'],
        header="exploration/")
    exploit_gan.launch(
        train_data, val_data, logger, config['initial_epochs'],
        header="exploitation/")

    # prevent the temperature from being annealed further
    if config['is_discrete']:
        explore_gan.start_temp = explore_gan.final_temp
        exploit_gan.start_temp = exploit_gan.final_temp

    # sample designs from the GAN and evaluate them
    condition_ys = tf.tile(tf.reduce_max(
        y, keepdims=True), [config['solver_samples'], 1])

    # generate samples for exploitation
    solver_xs = explore_gen.sample(condition_ys, temp=0.001)
    actual_ys = task.score(solver_xs)

    # record score percentiles
    logger.record("exploration/condition_ys",
                  condition_ys, 0, percentile=True)
    logger.record("exploration/actual_ys",
                  actual_ys, 0, percentile=True)

    # generate samples for exploitation
    solver_xs = exploit_gen.sample(condition_ys, temp=0.001)
    actual_ys = task.score(solver_xs)

    # record score percentiles
    logger.record("exploitation/condition_ys",
                  condition_ys, 0, percentile=True)
    logger.record("exploitation/actual_ys",
                  actual_ys, 0, percentile=True)

    # train the gan using an importance sampled data set
    for iteration in range(1, 1 + config['iterations']):

        # generate synthetic x paired with high performing scores
        tilde_x, tilde_y = get_synthetic_data(
            x, y,
            exploration_samples=config['exploration_samples'],
            exploration_rate=config['exploration_rate'],
            base_temp=base_temp)

        # build a weighted data set using newly collected samples
        train_data, val_data = task.build(
            x=tilde_x.numpy(), y=tilde_y.numpy(),
            importance_weights=get_weights(tilde_y.numpy(), base_temp=base_temp),
            batch_size=config['gan_batch_size'],
            val_size=config['val_size'])

        # train the gan for several epochs
        explore_gan.launch(
            train_data, val_data, logger, config['epochs_per_iteration'],
            start_epoch=config['epochs_per_iteration'] * iteration +
                        config['initial_epochs'],
            header="exploration/")

        # sample designs from the GAN and evaluate them
        condition_ys = tf.tile(tf.reduce_max(
            tilde_y, keepdims=True), [config['thompson_samples'], 1])

        # generate samples for exploration
        solver_xs = explore_gen.sample(condition_ys, temp=0.001)
        actual_ys = ensemble.get_distribution(solver_xs).mean() \
            if config['fully_offline'] else task.score(solver_xs)

        # record score percentiles
        logger.record("exploration/condition_ys",
                      condition_ys, iteration, percentile=True)
        logger.record("exploration/actual_ys",
                      actual_ys, iteration, percentile=True)

        # concatenate newly paired samples with the existing data set
        x = tf.concat([x, solver_xs], 0)
        y = tf.concat([y, actual_ys], 0)

        # build a weighted data set using newly collected samples
        train_data, val_data = task.build(
            x=x.numpy(), y=y.numpy(),
            importance_weights=get_weights(y.numpy(), base_temp=base_temp),
            batch_size=config['gan_batch_size'],
            val_size=config['val_size'])

        # train the gan for several epochs
        exploit_gan.launch(
            train_data, val_data, logger, config['epochs_per_iteration'],
            start_epoch=config['epochs_per_iteration'] * iteration +
                        config['initial_epochs'],
            header="exploitation/")

        # sample designs from the GAN and evaluate them
        condition_ys = tf.tile(tf.reduce_max(
            y, keepdims=True), [config['solver_samples'], 1])

        # generate samples for exploitation
        solver_xs = exploit_gen.sample(condition_ys, temp=0.001)
        actual_ys = task.score(solver_xs)

        # record score percentiles
        logger.record("exploitation/condition_ys",
                      condition_ys, iteration, percentile=True)
        logger.record("exploitation/actual_ys",
                      actual_ys, iteration, percentile=True)
