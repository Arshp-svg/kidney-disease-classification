import os
from pathlib import Path
import logging

# Setting  up logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

projectname='cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.yaml",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    "config/config.yaml",
    "requirements.txt",
    "dvc.yaml",
    "params.yaml",
    "research/trials.ipynb",
    "setup.py",
    "templates/index.html"
    
]


for file in list_of_files:
    file_path = Path(file)
    filedir,filename=os.path.split(file_path)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")