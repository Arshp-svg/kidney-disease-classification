from cnnClassifier.config.configuration import ConfigManager
from cnnClassifier import logger
from cnnClassifier.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion"
class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_dataingestion_config()
        self.dataingestion = DataIngestion(config=self.config)
        logger.info(f"{STAGE_NAME} initialized with config: {self.config}")
    def main(self):
        try:
            self.dataingestion.download_data()
            self.dataingestion.unzip_data()
        except Exception as e:
            logger.error(f"Error occurred during data ingestion: {e}")


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f"{STAGE_NAME} completed successfully.")
    except Exception as e:
        logger.error(f"Error occurred during {STAGE_NAME}: {e}")
        raise e
