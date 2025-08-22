from cnnClassifier.config.configuration import ConfigManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
     pass


    def main():
        config = ConfigManager()
        eval_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(eval_config)
        model_evaluation.evaluation()
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")