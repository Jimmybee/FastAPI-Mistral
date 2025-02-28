import requests

url = "http://localhost:8000/generate"
payload = {"prompt": "Explain black holes.", "max_length": 150}

response = requests.post(url, json=payload)
print(response.json())
