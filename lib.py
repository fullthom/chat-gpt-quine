
import os
import aiohttp

API_KEY = os.environ.get("OPENAI_API_KEY")

async def get_next_iteration(prompt, model="gpt-3.5-turbo") -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_json = await response.json()
            import json
            print(json.dumps(response_json))
            return response_json["choices"][0]["message"]["content"].strip()