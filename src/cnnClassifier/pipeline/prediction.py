import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        try:
            model = load_model(os.path.join("models", "model.h5"))
            test_image = image.load_img(self.filename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = test_image / 255.0  # Normalize if required by your model

            result = np.argmax(model.predict(test_image), axis=1)
            # print(result)  # Remove or use logging

            if result[0] == 1:
                prediction = "The person has CKD"
            else:
                prediction = "The person does not have CKD"
            return [{"prediction": prediction}]
        except Exception as e:
            return [{"error": str(e)}]