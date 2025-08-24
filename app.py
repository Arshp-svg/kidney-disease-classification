from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from cnnClassifier.utils.common import DecodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientAPP:
    def __init__(self):
        self.filename="inputimg.jpg"
        self.classifier=PredictionPipeline(self.filename)
        

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def train():
     os.system("dvc repro")
     return "Training completed"
 
 
 

@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.json["image"]
    DecodeImage(data, ClAPP.filename)
    result = ClAPP.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    ClAPP = ClientAPP()

    app.run(host="0.0.0.0", port=8080)