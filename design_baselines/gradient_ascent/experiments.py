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
@click.option('--local-dir', type=str, default='gradient-ascent-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def dkitty(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on DKittyMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def ant(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on AntMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "AntMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def hopper(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on HopperController-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "HopperController-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def superconductor(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on Superconductor-FullyConnected-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "Superconductor-FullyConnected-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-chembl')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def chembl(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on ChEMBL-ResNet-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "ChEMBL-ResNet-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def gfp(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on GFP-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "GFP-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-tf-bind-8')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def tf_bind_8(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on TFBind8-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "TFBind8-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-utr')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def utr(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on UTR-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "UTR-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']],
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def dkitty_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on DKittyMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def ant_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on AntMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "AntMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def hopper_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on HopperController-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "HopperController-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def superconductor_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on Superconductor-FullyConnected-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "Superconductor-FullyConnected-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-chembl')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def chembl_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on ChEMBL-ResNet-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "ChEMBL-ResNet-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def gfp_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on GFP-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "GFP-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-tf-bind-8')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def tf_bind_8_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on TFBind8-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "TFBind8-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-utr')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def utr_mean_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on UTR-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "UTR-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'mean',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


#############


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-dkitty')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def dkitty_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on DKittyMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "DKittyMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-ant')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def ant_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on AntMorphology-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "AntMorphology-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-hopper')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def hopper_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on HopperController-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "HopperController-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-superconductor')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def superconductor_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on Superconductor-FullyConnected-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "Superconductor-FullyConnected-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-chembl')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def chembl_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on ChEMBL-ResNet-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "ChEMBL-ResNet-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-gfp')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def gfp_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on GFP-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "GFP-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-tf-bind-8')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def tf_bind_8_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on TFBind8-Exact-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "TFBind8-Exact-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})


@cli.command()
@click.option('--local-dir', type=str, default='gradient-ascent-utr')
@click.option('--cpus', type=int, default=24)
@click.option('--gpus', type=int, default=1)
@click.option('--num-parallel', type=int, default=1)
@click.option('--num-samples', type=int, default=1)
def utr_min_ensemble(local_dir, cpus, gpus, num_parallel, num_samples):
    """Evaluate Naive Gradient Ascent on UTR-Transformer-v0
    """

    # Final Version

    from design_baselines.gradient_ascent import gradient_ascent
    ray.init(num_cpus=cpus,
             num_gpus=gpus,
             include_dashboard=False,
             _temp_dir=os.path.expanduser('~/tmp'))
    tune.run(gradient_ascent, config={
        "logging_dir": "data",
        "task": "UTR-Transformer-v0",
        "task_kwargs": {},
        "normalize_ys": True,
        "normalize_xs": True,
        "model_noise_std": 0.0,
        "val_size": 200,
        "batch_size": 128,
        "epochs": 100,
        "activations": [['leaky_relu', 'leaky_relu']] * 5,
        "hidden_size": 2048,
        "initial_max_std": 0.2,
        "initial_min_std": 0.1,
        "forward_model_lr": 0.001,
        "aggregation_method": 'min',
        "solver_samples": 128,
        "solver_lr": 0.01,
        "solver_steps": 500},
        num_samples=num_samples,
        local_dir=local_dir,
        resources_per_trial={'cpu': cpus // num_parallel,
                             'gpu': gpus / num_parallel - 0.01})
