import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://ollama:11434")

def ask_ollama(prompt, model="tinyllama"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(f"{OLLAMA_API_URL}/api/generate", json=payload)
    return response.json()['response']

if __name__ == "__main__":
    print("Asking Ollama...")
    prompt = "What is the capital of France?"
    print(f"Prompt: {prompt}")
    result = ask_ollama(prompt)
    print(result)
