# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python buffering (for logging)
ENV PYTHONUNBUFFERED=1

# Create and set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the default command to run the Flask app using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "run:app"]
