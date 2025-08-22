from cnnClassifier.config.configuration import ConfigManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger


STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            config=ConfigManager()
            training_config=config.get_training_config()
            training=Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            print(f"Error occurred: {e}")
            


if __name__=="__main__":
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline=ModelTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
