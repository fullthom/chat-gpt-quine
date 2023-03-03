
import os
import aiohttp
import asyncio

API_KEY = os.environ.get("OPENAI_API_KEY")

async def get_next_iteration(prompt, model="gpt-3.5-turbo") -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_json = await response.json()
            return response_json["choices"][0]["message"]["content"].strip()
        

async def _get_chidren(prompt, n):
    tasks = [get_next_iteration(prompt) for _ in range(n)]
    return await asyncio.gather(*tasks)

def get_children(prompt, n, lineage):
    print(f"get_children start {lineage}")
    res = asyncio.run(_get_chidren(prompt, n))
    print(f"get_children end {lineage}")
    return res


