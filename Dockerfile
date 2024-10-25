# Dockerfile for a simple Python Flask app
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application files
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the application
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
