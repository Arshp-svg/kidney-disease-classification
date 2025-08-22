from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataingestionConfig:
    root_dir: Path
    source_url: str
    local_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    image_size: list
    batch_size: int
    include_top: bool
    classes: int
    weights: str
    epochs: int
    learning_rate: float



@dataclass
class TrainingConfig:
   root_dir: Path
   model_checkpoint: Path
   updated_base_model_path:Path
   training_data:Path
   params_epoch:int
   params_batch_size:int
   params_image_size:list
   params_augmentation:bool


@dataclass(frozen=True)
class ModelEvaluationConfig:
    model_path: Path
    train_data_path: Path
    all_params: dict
    mlflow_tracking_uri: str
    params_image_size: list
    params_batch_size: int