from dataclasses import dataclass
from pathlib import Path
import logging

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL : str
    local_data_file: Path
    unzip_dir: Path
    
logging.info("data ingestion variables created")



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
logging.info("base model variables created")


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    
logging.info("callback variables created")


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

logging.info("training variables created")


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    params_image_size: list
    params_batch_size: int
    
logging.info("evalution variables created")