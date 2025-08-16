import os
from box.exceptions import BoxValueError
from cnnClassifier import logger
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    with open(path_to_yaml, "r") as file:
        content = yaml.safe_load(file)
        print("YAML content loaded:", content)
        if content is None:
            raise ValueError(f"YAML file {path_to_yaml} is empty or invalid.")
        return ConfigBox(content)
    


@ensure_annotations
def create_directories(dirs: list, verbose=True):
    for dir in dirs:
        try:
            os.makedirs(dir, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {dir}")
        except Exception as e:
            logger.error(f"Error creating directory {dir}: {e}")


@ensure_annotations
def save_json(data: Any, path: Path) -> None:
    try:
        with open(path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logger.error(f"Error saving JSON to {path}: {e}")
        raise e
    

@ensure_annotations
def load_json(path: Path) -> Any:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error loading JSON from {path}: {e}")
        raise e
    
@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    try:
        joblib.dump(data, path)
        logger.info(f"Saved binary data to {path}")
    except Exception as e:
        logger.error(f"Error saving binary to {path}: {e}")
        raise e


@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        return joblib.load(path)
    except Exception as e:
        logger.error(f"Error loading binary from {path}: {e}")
        raise e


@ensure_annotations
def get_file_size(path: Path) -> str:
    size_in_kb=round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"


def DecodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def EncodeImage(filename):
    with open(filename, "rb") as image_file:
        return base64.b64encode(image_file.read())
