import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_file_size
from cnnClassifier.entity.config_entity import DataingestionConfig


class DataIngestion:
    def __init__(self, config: DataingestionConfig):
        self.config = config
        
        

    def download_data(self):
        try:
            dataset_url = self.config.source_url
            zip_download_path = self.config.local_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to {zip_download_path}")
            # Extract file ID from the URL
            file_id = dataset_url.split("/")[-2]
            gdown.download(f"https://drive.google.com/uc?id={file_id}", zip_download_path, quiet=False)
            logger.info(f"Data downloaded successfully to {zip_download_path}")
        except Exception as e:
            raise e
       
       
       
       
    def unzip_data(self):
        if not zipfile.is_zipfile(self.config.local_file):
            logger.error(f"{self.config.local_file} is not a valid zip file.")
            raise zipfile.BadZipFile(f"{self.config.local_file} is not a valid zip file.")
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        logger.info("Unzipping data...")
        with zipfile.ZipFile(self.config.local_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            
            