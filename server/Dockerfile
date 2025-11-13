# Use a lightweight official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Create uploads directory if it doesn't exist
RUN mkdir -p uploads

# Expose Flask port
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV FLASK_ENV=development

# Run Flask app
CMD ["python", "app.py"]
