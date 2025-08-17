from cnnClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnClassifier.utils.common import create_directories,read_yaml
from cnnClassifier.entity.config_entity import DataingestionConfig,PrepareBaseModelConfig


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