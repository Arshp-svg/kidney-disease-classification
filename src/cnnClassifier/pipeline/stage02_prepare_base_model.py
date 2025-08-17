from cnnClassifier.config.configuration import ConfigManager
from cnnClassifier import logger
from cnnClassifier.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f"Starting {STAGE_NAME}...")
        config=ConfigManager()
        prepare_base_model=config.get_model_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        logger.info(f"Completed {STAGE_NAME}.")
    
    

if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}...")
        obj=PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}.")
    except Exception as e:
        logger.error(f"Error occurred in {STAGE_NAME}: {e}")