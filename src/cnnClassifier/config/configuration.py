from cnnClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnClassifier.utils.common import create_directories,read_yaml
from cnnClassifier.entity.config_entity import DataingestionConfig,PrepareBaseModelConfig,ModelEvaluationConfig
from cnnClassifier.entity.config_entity import TrainingConfig
import os

class ConfigManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        
        create_directories([self.config.artifacts_root])
        
    
    def get_dataingestion_config(self) -> DataingestionConfig:
       config=self.config.data_ingestion
       
       create_directories([config.root_dir])

       data_ingestion_config = DataingestionConfig(
           root_dir=config.root_dir,
           source_url=config.source_url,
           local_file=config.local_file,
           unzip_dir=config.unzip_dir
       )

       return data_ingestion_config
   
   
    def get_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            image_size=self.params.IMAGE_SIZE,
            batch_size=self.params.BATCH_SIZE,
            include_top=self.params.INCLUDE_TOP,
            classes=self.params.CLASSES,
            weights=self.params.WEIGHTS,
            epochs=self.params.EPOCHS,
            learning_rate=self.params.LEARNING_RATE
        )

        return base_model_config
    
    
    def get_training_config(self) -> TrainingConfig:
        training=self.config.training
        prepare_base_model=self.config.prepare_base_model
        
        params=self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"kidney-ct-scan-image")
        
        create_directories([training.root_dir])
        
        training_config = TrainingConfig(
            root_dir=training.root_dir,
            model_checkpoint=training.model_checkpoint,
            updated_base_model_path=prepare_base_model.updated_base_model_path,
            training_data=training_data,
            params_epoch=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_image_size=params.IMAGE_SIZE,
            params_augmentation=params.AUGMENTATION
        )

        return training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        evaluation_config = ModelEvaluationConfig(
            model_path="artifacts/training/model.h5",
            train_data_path="artifacts/data_ingestion/kidney-ct-scan-image",
            all_params=self.params,
            mlflow_tracking_uri="https://dagshub.com/arshpatel213/kidney-disease-classification.mlflow",
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return evaluation_config