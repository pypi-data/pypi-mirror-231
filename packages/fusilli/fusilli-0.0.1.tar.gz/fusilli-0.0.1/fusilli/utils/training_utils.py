"""
Functions for initializing the pytorch lightning logger and trainer.
"""

import wandb
from pytorch_lightning.loggers import TensorBoardLogger, WandbLogger
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning import Trainer
from tqdm import tqdm
from pytorch_lightning.callbacks import TQDMProgressBar
import os
import torch.nn as nn


def set_logger(params, fold, fusion_model, extra_log_string_dict=None):
    """
    Set the logger for the current run. If params["log"] is True, then the logger is set to
    WandbLogger, otherwise it is set to None.

    Args:
        params (dict): Dictionary of parameters.
        fold (int): Fold number.
        fusion_model (class): Fusion model class.
        extra_string_dict (dict): Extra string to add to the run name. e.g. if you're running
            the same model with different hyperparameters, you can add the hyperparameters.
            Input format {"name": "value"}. In the run name, the extra string will be added
            as "name_value". And a tag will be added as "name_value".

    Returns:
        logger (object): Pytorch lightning logger object.
    """
    method_name = fusion_model.__class__.__name__
    modality_type = fusion_model.modality_type
    fusion_type = fusion_model.fusion_type

    if extra_log_string_dict is not None:
        extra_name_string = ""
        extra_tags = []
        for key, value in extra_log_string_dict.items():
            extra_name_string += f"_{key}_{str(value)}"
            extra_tags.append(f"{key}_{str(value)}")
    else:
        extra_name_string = ""
        extra_tags = []

    if params["kfold_flag"]:
        name = f"{method_name}_fold_{fold}{extra_name_string}"
        tags = [modality_type, fusion_type, f"fold_{str(fold)}"] + extra_tags
    else:
        name = f"{method_name}{extra_name_string}"
        tags = [modality_type, fusion_type] + extra_tags

    if params["log"]:
        logger = WandbLogger(
            save_dir=os.getcwd() + "/logs",
            project=params["timestamp"],
            name=name,
            tags=tags,
            log_model=True,
            group=method_name,
            reinit=True,
        )
        logger.experiment.config["method_name"] = method_name
        if extra_log_string_dict is not None:
            for key, value in extra_log_string_dict.items():
                logger.experiment.config[key] = value

    else:
        logger = None

    return logger


class LitProgressBar(TQDMProgressBar):
    def init_validation_tqdm(self):
        bar = tqdm(
            disable=True,
        )
        return bar


def init_trainer(logger, max_epochs=1000, enable_checkpointing=True):
    """
    Initialize the pytorch lightning trainer object.

    Args:
        logger (object): Pytorch lightning logger object.
        max_epochs (int): Maximum number of epochs.
        enable_checkpointing (bool): Whether to enable checkpointing. If True, then
            checkpoints will be saved. We use False for the example notebooks in the
            repository/documentation.

    Returns:
        trainer (object): Pytorch lightning trainer object.
    """

    early_stop_callback = EarlyStopping(
        monitor="val_loss",
        min_delta=0.00,
        patience=15,
        verbose=False,
        mode="min",
    )

    bar = LitProgressBar()

    trainer = Trainer(
        max_epochs=max_epochs,
        num_sanity_val_steps=0,
        # accelerator="mps",
        devices=1,
        callbacks=[early_stop_callback, bar],
        log_every_n_steps=2,
        # default_root_dir=run_dir,
        logger=logger,
        enable_checkpointing=enable_checkpointing,
    )

    return trainer


def get_final_val_metrics(trainer):
    """
    Get the final validation metrics from the trainer object.

    Args:
        metric_names (list): List of metric names.
        trainer (object): Pytorch lightning trainer object.

    Returns:
        metric1 (float): Final validation metric 1.
        metric2 (float): Final validation metric 2.
    """
    metric_names = trainer.model.metric_names_list
    metric1 = trainer.callback_metrics[f"{metric_names[0]}_val"].item()
    metric2 = trainer.callback_metrics[f"{metric_names[1]}_val"].item()

    return metric1, metric2
