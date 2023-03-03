
import os
import requests

API_KEY = os.environ.get("OPENAI_API_KEY")

def create_chat_completion(prompt, model="gpt-3.5-turbo") -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()
