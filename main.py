from cnnClassifier.pipeline.stag01_data_ingestion import DataIngestionPipeline
from cnnClassifier import logger

if __name__ == "__main__":
    try:
        logger.info("Starting Data Ingestion...")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info("Data Ingestion completed successfully.")
    except Exception as e:
        logger.error(f"Error occurred during Data Ingestion: {e}")
        raise e
