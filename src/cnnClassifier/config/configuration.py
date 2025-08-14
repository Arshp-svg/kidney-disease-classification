from cnnClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnClassifier.utils.common import create_directories,read_yaml
from cnnClassifier.entity.config_entity import DataingestionConfig

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