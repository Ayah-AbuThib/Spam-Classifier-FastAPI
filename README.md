
# Spam Classifier API with FastAPI and Docker🐳

This repository contains a machine learning-based API that classifies whether a given message is spam or not. The model is trained using **scikit-learn** and **joblib** for serialization, and the entire project is deployed using **FastAPI**. It is fully **Dockerized** to ensure seamless deployment across different environments.

### 🚀 **Quick Start**

To get the application running locally, follow the steps below.

1. **Pull the pre-built Docker image** from Docker Hub:
   ```bash
   docker pull ayahabuthib/fastapi-app
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:80 ayahabuthib/fastapi-app
   ```
   This will start the FastAPI server on `http://localhost:8000`.

3. **Access the API documentation**:
   Once the application is running, navigate to `http://localhost:8000/docs` to interact with the API via an auto-generated, user-friendly interface powered by Swagger.

---

### 🛠️ **Features**

- **Data Preprocessing**: Leverages **pandas** for data manipulation and **scikit-learn** for model preprocessing (e.g., text vectorization using `CountVectorizer`).
  
- **Model Training**: A **spam classifier** is trained using **scikit-learn** and serialized with **joblib** for efficient model loading and inference.

- **API Deployment**: The trained model is exposed as an API using **FastAPI**, providing endpoints to classify messages as spam or not.

- **Dockerized**: The entire application is encapsulated in a **Docker** container for easy, scalable deployment.

- **Model Inference**: Classifies input text through a `POST` request. It returns whether the message is **spam** or **ham** (non-spam).

---

### 📦 **Installation & Setup**

#### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.11+**
- **Docker**: for containerization and deployment
- **Required Python Libraries**: You can install the required dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```

#### Steps for Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/ayahabuthib/spam-classifier-fastapi-docker.git
   cd spam-classifier-fastapi-docker
   ```

2. Install dependencies (if you are not using Docker):
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI app:
   ```bash
   uvicorn app.main:app --reload
   ```
   This will run the app locally at `http://localhost:8000`.

---

### 🚢 **Dockerized Deployment**

To build and run the application inside a Docker container:

1. **Build the Docker image**:
   ```bash
   docker build -t fastapi-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:80 fastapi-app
   ```
   You can now access the API at `http://localhost:8000`.

---

### 🧑‍💻 **API Endpoints**

#### `/predict` (POST)

Classifies a given message as spam or not.

- **Request Body**:
  ```json
  {
    "message": "Free money now!"
  }
  ```

- **Response**:
  ```json
  {
    "prediction": "spam"
  }
  ```

---

### 🔧 **Customizing the Model**

- **Training a new model**: If you'd like to retrain the spam classifier with your own data:
  1. Prepare your dataset with labeled examples of spam and ham.
  2. Update the model training code in `train_model.py`.
  3. Retrain the model and save it using `joblib`.
  4. Replace the old model in the `model` directory with the new one.

- **Modifying Preprocessing**: You can tweak the text preprocessing steps (like vectorizer parameters) in the `preprocess.py` file to improve the accuracy or performance.

---

### 🛠️ **Tech Stack**

- **FastAPI**: Lightweight and fast framework for building APIs.
- **scikit-learn**: Machine learning library used for training the spam classifier.
- **joblib**: Used for serializing the trained model to disk.
- **Docker**: For containerization and deployment.
- **Uvicorn**: ASGI server to run FastAPI.
