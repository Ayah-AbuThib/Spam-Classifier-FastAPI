FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /code 

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the entire application (excluding the files defined in .dockerignore) into the container
COPY ./app /code/app

COPY spam_classifier.joblib /code/
# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]