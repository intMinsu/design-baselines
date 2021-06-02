from ray import tune
import click
import ray
import os


@click.group()
def cli():
    """A group of experiments for training Conservative Score Models
    and reproducing our ICLR 2021 results.
    """


#############


@cli.command()
@click.option('--local-dir', type=str, default='mins-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on DKittyMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-Exact-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": True,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0,
        "pool_size": 0,
        "pool_frac": 0,
        "pool_save": 0,
        "fake_pair_frac": 0.,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on AntMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "AntMorphology-Exact-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": True,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0,
        "pool_size": 0,
        "pool_frac": 0,
        "pool_save": 0,
        "fake_pair_frac": 0.,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def hopper(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on HopperController-Exact-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "HopperController-Exact-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": True,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0,
        "pool_size": 0,
        "pool_frac": 0,
        "pool_save": 0,
        "fake_pair_frac": 0.,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 500,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
@click.option('--oracle', type=str, default="RandomForest")
def superconductor(local_dir, cpus, gpus, num_parallel, num_samples, oracle):
    """Evaluate MINs on Superconductor-RandomForest-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": f"Superconductor-{oracle}-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": True,
        "base_temp": 0.1,
        "noise_std": 0.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0,
        "pool_size": 0,
        "pool_frac": 0,
        "pool_save": 0,
        "fake_pair_frac": 0.,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-chembl')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def chembl(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on ChEMBL-ResNet-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "ChEMBL-ResNet-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": False,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 1.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0.,
        "pool_size": 0,
        "pool_frac": 0.,
        "pool_save": 0,
        "fake_pair_frac": 0.0,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
@click.option('--oracle', type=str, default="Transformer")
def gfp(local_dir, cpus, gpus, num_parallel, num_samples, oracle):
    """Evaluate MINs on GFP-Transformer-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": f"GFP-{oracle}-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": False,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 1.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0.,
        "pool_size": 0,
        "pool_frac": 0.,
        "pool_save": 0,
        "fake_pair_frac": 0.0,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-tf-bind-8')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def tf_bind_8(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on TFBind8-Exact-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "TFBind8-Exact-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": False,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 1.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0.,
        "pool_size": 0,
        "pool_frac": 0.,
        "pool_save": 0,
        "fake_pair_frac": 0.0,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='mins-utr')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def utr(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate MINs on UTR-Transformer-v0
    """

    # Final Version

    from design_baselines.mins import mins
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(mins, config={
        "logging_dir": "data",
        "task": "UTR-Transformer-v0",
        "task_kwargs": {"relabel": False},
        "val_size": 200,
        "offline": True,
        "normalize_ys": True,
        "normalize_xs": False,
        "base_temp": 0.1,
        "keep": 0.99,
        "start_temp": 5.0,
        "final_temp": 1.0,
        "method": "wasserstein",
        "gan_batch_size": 128,
        "hidden_size": 1024,
        "num_layers": 1,
        "bootstraps": 1,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "oracle_lr": 0.001,
        "oracle_batch_size": 128,
        "oracle_epochs": 100,
        "latent_size": 32,
        "critic_frequency": 10,
        "flip_frac": 0.,
        "pool_size": 0,
        "pool_frac": 0.,
        "pool_save": 0,
        "fake_pair_frac": 0.0,
        "penalty_weight": 10.,
        "generator_lr": 2e-4,
        "generator_beta_1": 0.0,
        "generator_beta_2": 0.9,
        "discriminator_lr": 2e-4,
        "discriminator_beta_1": 0.0,
        "discriminator_beta_2": 0.9,
        "initial_epochs": 200,
        "epochs_per_iteration": 0,
        "iterations": 0,
        "exploration_samples": 0,
        "exploration_rate": 0.,
        "thompson_samples": 0,
        "solver_samples": 128},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})

