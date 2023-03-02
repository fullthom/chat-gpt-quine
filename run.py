import requests
import json
import re
import logging
import os
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("log.txt")
file_handler.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(funcName)s:%(lineno)d - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

API_KEY = os.environ.get("OPENAI_API_KEY")

DELIMITER = "# @@" + "@"


def create_chat_completion(prompt, model="gpt-3.5-turbo"):
    logger.debug("Start of create_chat_completion")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data)
    logger.debug("End of create_chat_completion")
    if response.status_code == 200:
        res = response.json()
        logger.debug("API Response: " + json.dumps(res))
        return res
    else:
        msg = "Request to API failed!"
        logger.error(msg)
        raise Exception(msg)


def get_prompt() -> str:
    with open("prompt.txt", "r") as f:
        prompt = f.read()

    with open("run.py", "r") as f:
        code = f.read()

    return prompt + code


def write_prompt(prompt: str) -> None:
    with open("prompt.txt", "w") as f:
        f.write(prompt)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def get_code_from_completion_response(response: dict) -> str:
    content = response["choices"][0]["message"]["content"].strip()
    logger.debug("Full Response Content: " + content)

    # Extract the first code from the response
    re_res = re.findall(r"(```\n|```python\n)([\s\S]+?)```", content)
    logger.debug(re_res)
    if len(re_res) > 0:
        code = re_res[0][1]
    else:
        # Maybe the entire response is code?
        code = content
    code = (
        code.removeprefix("```")
        .removeprefix("python")
        .removesuffix("```")
        .replace(DELIMITER, "")
    )
    logger.info("Extracted Code: " + code)
    assert "```" not in code
    return code


def run():
    logger.warning("Start of run()")
    prompt = get_prompt()
    logger.debug("Using prompt: " + prompt)
    
    code = None
    while code is None:
        res = create_chat_completion(prompt)
        try:
            code = get_code_from_completion_response(res)
        except AssertionError as e:
            logging.warning(e)

    logger.info("Writing to run.py")
    with open("run.py", "r") as f:
        old = f.read()
        with open("run.py", "w") as f2:
            chunks = old.split(DELIMITER)
            if "DELETE EXISTING CODE!" in code:
                chunks[1] = ""

            f2.write(
                (
                    chunks[0]
                    + DELIMITER
                    + chunks[1]
                    + "\n" 
                    + code
                    + DELIMITER
                    + chunks[2]
                )
            )

    logger.info("Finished updating run.py")


# @@@


# @@@

if __name__ == "__main__":
    run()
    restart_program()
