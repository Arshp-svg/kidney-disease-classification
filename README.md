# 🏥 Kidney Disease Classification using Deep Learning

A complete end-to-end deep learning pipeline for classifying kidney CT scan images, built with TensorFlow, DVC, and MLflow.  This project implements a modular ML workflow with automated training pipelines and real-time prediction API.

## 📊 Project Overview

This project uses transfer learning with VGG16 to classify kidney CT scan images into different categories.  The entire workflow is managed using DVC (Data Version Control) for reproducibility and MLflow for experiment tracking.

**Model Performance:**
- 📈 **Accuracy**: 94.62%
- 📉 **Loss**: 0.113

## ✨ Features

- **Modular Pipeline Architecture**: Clean separation of data ingestion, model preparation, training, and evaluation
- **Transfer Learning**:  Utilizes pre-trained VGG16 model with ImageNet weights
- **DVC Integration**: Version control for data and model artifacts
- **MLflow Tracking**:  Experiment tracking and model registry
- **REST API**: Flask-based API for predictions
- **Docker Support**: Containerized deployment
- **Data Augmentation**: Built-in image augmentation for robust training

## 🛠️ Tech Stack

- **Deep Learning**: TensorFlow 2.12. 0
- **Web Framework**: Flask with CORS support
- **Experiment Tracking**: MLflow 2.2.2
- **Version Control**: DVC
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Configuration**: PyYAML, python-box

## 📁 Project Structure

```
kidney-disease-classification/
├── . github/workflows/          # CI/CD workflows
├── artifacts/                  # Generated artifacts (models, data)
├── config/
│   └── config.yaml            # Configuration file
├── models/                    # Saved models
├── research/                  # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── src/cnnClassifier/
│   ├── components/            # Core components
│   │   ├── data_ingestion.py
│   │   ├── model_training.py
│   │   └── model_evaluation.py
│   ├── config/
│   │   └── configuration.py   # Configuration manager
│   ├── entity/
│   │   └── config_entity.py   # Data classes
│   ├── pipeline/              # Pipeline stages
│   │   ├── stag01_data_ingestion. py
│   │   ├── stage02_prepare_base_model. py
│   │   ├── stage03_model_training. py
│   │   └── stage04_model_evaluation.py
│   ├── utils/                 # Utility functions
│   └── constants/             # Constants
├── templates/
│   └── index.html            # Web interface
├── app.py                    # Flask application
├── main.py                   # Main pipeline runner
├── dvc.yaml                  # DVC pipeline definition
├── params.yaml               # Model hyperparameters
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
└── Dockerfile               # Docker configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- DVC
- (Optional) Docker

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arshp-svg/kidney-disease-classification.git
   cd kidney-disease-classification
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package**
   ```bash
   pip install -e .
   ```

### Configuration

The project uses two main configuration files:

**`config/config.yaml`**: Defines paths and data sources
**`params.yaml`**: Contains model hyperparameters

```yaml
# params.yaml
AUGMENTATION: True
IMAGE_SIZE: [224, 224, 3]
BATCH_SIZE:  16
INCLUDE_TOP:  False
EPOCHS: 1
CLASSES: 2
WEIGHTS: imagenet
LEARNING_RATE: 0.01
```

## 📝 Usage

### Training the Model

#### Option 1: Run Complete Pipeline
```bash
python main.py
```

#### Option 2: Run with DVC
```bash
dvc repro
```

#### Option 3: Run Individual Stages
```bash
# Data ingestion
python src/cnnClassifier/pipeline/stag01_data_ingestion.py

# Prepare base model
python src/cnnClassifier/pipeline/stage02_prepare_base_model.py

# Train model
python src/cnnClassifier/pipeline/stage03_model_training.py

# Evaluate model
python src/cnnClassifier/pipeline/stage04_model_evaluation.py
```

### Running the Web Application

```bash
python app.py
```

The application will be available at `http://localhost:8080`

### API Endpoints

- **`GET /`**: Web interface for image upload
- **`GET/POST /train`**: Trigger model training pipeline
- **`POST /predict`**: Make predictions on uploaded images

#### Example Prediction Request
```python
import requests
import base64

# Read and encode image
with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f. read()).decode()

# Make prediction
response = requests.post(
    "http://localhost:8080/predict",
    json={"image": image_data}
)
print(response.json())
```

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t kidney-disease-classifier .
```

### Run Container
```bash
docker run -p 8080:8080 kidney-disease-classifier
```

## 📊 MLflow Tracking

This project uses MLflow for experiment tracking.  The tracking URI is configured in the code:

```
https://dagshub.com/arshpatel213/kidney-disease-classification. mlflow
```

View experiments, compare metrics, and manage model versions through the MLflow UI.

## 🔄 DVC Pipeline

The DVC pipeline consists of four stages:

1. **Data Ingestion**: Download and extract kidney CT scan dataset
2. **Prepare Base Model**: Load and configure VGG16 base model
3. **Train Model**: Fine-tune model with data augmentation
4. **Evaluate Model**: Assess model performance and log metrics

To reproduce the entire pipeline:
```bash
dvc repro
```

## 📈 Model Architecture

- **Base Model**: VGG16 (pre-trained on ImageNet)
- **Input Shape**: 224x224x3
- **Transfer Learning**: Feature extraction + fine-tuning
- **Classes**: 2 (configurable)
- **Optimizer**:  Configured in base model preparation
- **Data Augmentation**: 
  - Rotation (40°)
  - Width/Height shift (20%)
  - Shear (20%)
  - Zoom (20%)

## 🧪 Research Notebooks

Explore the `research/` directory for detailed experimentation:

- `01_data_ingestion.ipynb`: Data loading and exploration
- `02_prepare_base_model.ipynb`: Model architecture setup
- `03_model_training.ipynb`: Training experiments
- `04_model_evaluation.ipynb`: Performance analysis

## 📦 Package Information

**Package Name**: `cnnClassifier`  
**Version**: 0.0.1  
**Author**: Arshp-svg  
**Email**: arshpatel213@gmail.com

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. 

## 🙏 Acknowledgments

- VGG16 architecture by Visual Geometry Group, Oxford
- TensorFlow and Keras teams
- DVC and MLflow communities

## 📧 Contact

**Arsh Patel**  
- GitHub: [@Arshp-svg](https://github.com/Arshp-svg)
- Email: arshpatel213@gmail.com

## 🔗 Links

- [Repository](https://github.com/Arshp-svg/kidney-disease-classification)

---

**⭐ If you find this project helpful, please consider giving it a star! **
