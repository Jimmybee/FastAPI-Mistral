# ==========================================
# Dockerfile for FastAPI Mistral 7B Application
# ==========================================
#
# How to build:
#   docker build -t mistral-api .
#
# How to run:
#   docker run -p 8000:8000 --env-file .env mistral-api
#   
# For production:
#   docker run -p 8000:8000 -e HF_TOKEN=your_token mistral-api
#
# SECURITY NOTE: Never include sensitive tokens directly in this Dockerfile,
# always pass them as environment variables at runtime.

# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Create a non-root user for improved security
RUN adduser --disabled-password --gecos "" appuser

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
# Note: Create a .dockerignore file with entries for .env, __pycache__, etc.
# to avoid copying sensitive or unnecessary files
COPY . .

# Set ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the port FastAPI runs on
EXPOSE 8000

# Environment variables (defaults for non-sensitive values)
ENV PORT=8000

# Run the FastAPI app
# Using 0.0.0.0 allows connections from any IP address
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
