# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and the trained model
# (Assumes your train.py saves the model to model.pkl)
COPY app/ /app/app/
COPY model.pkl /app/

# Expose the port your app runs on (e.g., 5000 for Flask/FastAPI)
EXPOSE 5000

# Command to run the application
CMD ["python", "app/app.py"]