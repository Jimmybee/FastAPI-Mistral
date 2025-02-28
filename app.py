from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

app = FastAPI()

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

HF_TOKEN = os.getenv("HF_TOKEN")
# Detect the best available device
if torch.backends.mps.is_available():
    device = "mps"  # Apple Silicon (Mac M1/M2)
elif torch.cuda.is_available():
    device = "cuda"  # NVIDIA GPU
else:
    device = "cpu"   # Fallback

print(f"Loading model on {device}...")

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device in ["cuda", "mps"] else torch.float32,
    device_map="auto"
).to(device)

# Define request schema
class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 200  # Optional

@app.post("/generate")
async def generate_text(request: PromptRequest):
    try:
        inputs = tokenizer(request.prompt, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}  # Move input to model's device

        outputs = model.generate(**inputs, max_length=request.max_length, pad_token_id=tokenizer.eos_token_id)
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": response_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
