# FastAPI-Mistral

A robust API service that integrates Mistral AI's language models with FastAPI to provide a scalable, efficient, and easy-to-use interface for AI-powered applications.

## Project Description

FastAPI-Mistral is a modern web service that allows developers to interact with Mistral AI's powerful language models through a clean RESTful API. The project leverages FastAPI's async capabilities and automatic documentation features to provide a high-performance, developer-friendly experience when working with state-of-the-art language models.

Key features:
- Seamless integration with Mistral AI models
- Asynchronous request handling for improved performance
- Comprehensive API documentation via Swagger UI
- Configurable model parameters and request settings
- Rate limiting and caching capabilities
- Structured response formatting

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/FastAPI-Mistral.git
   cd FastAPI-Mistral
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # On Windows
   copy .env.example .env
   
   # On macOS/Linux
   cp .env.example .env
   ```
   
5. Edit the `.env` file to add your Mistral API key and configure other settings.

## Usage Examples

### Starting the Server

```bash
uvicorn app:app --reload
```

The API will be available at http://localhost:8000, and the interactive documentation can be accessed at http://localhost:8000/docs.

### Basic API Requests

#### Text Generation

```python
import requests

response = requests.post(
    "http://localhost:8000/generate",
    json={
        "prompt": "Explain quantum computing in simple terms",
        "max_tokens": 150,
        "temperature": 0.7
    }
)

print(response.json())
```

#### Model Information

```python
import requests

response = requests.get("http://localhost:8000/models")
print(response.json())
```

### Using the Streaming API

```python
import requests
import json

response = requests.post(
    "http://localhost:8000/generate/stream",
    json={
        "prompt": "Write a short story about a robot learning to paint",
        "max_tokens": 500
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        data = json.loads(line.decode('utf-8'))
        print(data['text'], end='', flush=True)
```

## Requirements

### Python Version
- Python 3.9 or higher

### Dependencies
- fastapi>=0.95.0
- pydantic>=2.0.0
- uvicorn>=0.22.0
- python-dotenv>=1.0.0
- httpx>=0.24.0
- tenacity>=8.2.2
- mistralai>=0.0.1

## API Documentation

Once the server is running, visit http://localhost:8000/docs for comprehensive API documentation, including:

- Available endpoints
- Request/response schemas
- Authentication requirements
- Interactive API testing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

