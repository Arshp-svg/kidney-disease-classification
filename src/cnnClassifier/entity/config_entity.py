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
    