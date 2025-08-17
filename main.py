from cnnClassifier.pipeline.stag01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion"

try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME}.")
except Exception as e:
        logger.error(f"Error occurred during {STAGE_NAME}: {e}")
        raise e



STAGE_NAME = "Prepare Base Model"

try:
        logger.info(f"Starting {STAGE_NAME}...")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}.")
except Exception as e:
        logger.error(f"Error occurred in {STAGE_NAME}: {e}")
        raise e