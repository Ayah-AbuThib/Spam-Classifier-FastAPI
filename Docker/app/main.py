from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np

# Load the spam classifier model
try:
    spam_model = joblib.load('spam_classifier.joblib')
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Welcome to the Spam Detection API'}

# Define the request schema for the prediction input
class InputData(BaseModel):
    message: str  # Input message to classify as spam or not

# Endpoint for prediction
@app.post("/predict")
async def predict(data: InputData):
    try:
        # Create a numpy array with the input message
        input_data = np.array([data.message])
        
        # Make a prediction using the loaded model
        prediction = spam_model.predict(input_data)
        
        # Return the prediction as a response
        return {"prediction": int(prediction[0]), "label": "spam" if prediction[0] == 1 else "ham"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app)