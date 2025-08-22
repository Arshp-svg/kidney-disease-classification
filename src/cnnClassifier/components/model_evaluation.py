import tensorflow as tf
from pathlib import Path
import mlflow
from cnnClassifier.utils.common import save_json
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import ModelEvaluationConfig




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def train_valid_generator(self):

        ## data generator copied from keras documentation
        datagenerator_kwargs=dict(
            rescale=1./255,
            validation_split=0.2
        )

        dataflow_kwargs=dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
    

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator=valid_datagenerator.flow_from_directory(
            directory=self.config.train_data_path,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
    @staticmethod
    def load_model(model_path: str) -> tf.keras.Model:
        model = tf.keras.models.load_model(model_path)
        return model
    
    
    def evaluation(self):
        self.model = self.load_model(self.config.model_path)
        self.train_valid_generator()
        self.results = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores={"loss": self.results[0], "accuracy": self.results[1]}
        save_json(path=Path("scores.json"), data=scores)
    
    
    def log_into_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.results[0], "accuracy": self.results[1]})
            
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="KidneyDiseaseModel")
            else:
                mlflow.keras.log_model(self.model, "model")
                
