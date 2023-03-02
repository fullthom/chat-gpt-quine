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
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

API_KEY = ""


# @@@

# @@@


def create_chat_completion(prompt, model="gpt-3.5-turbo"):
    logger.debug("Start of create_chat_completion")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data)
    logger.debug("End of create_chat_completion")
    if response.status_code == 200:
        logger.debug("API Response: " + json.dumps(response))
        return response.json()
    else:
        msg = "Request to API failed!"
        logger.error(msg)
        raise Exception(msg)


def read_prompt() -> str:
    with open("prompt.txt", "r") as f:
        return "\n".join(f.readlines())


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
    re_res = re.findall(r"```\n([\s\S]+?)```", content)
    logger.debug(re_res)
    if len(re_res) > 0:
        code = re_res[0]
    else:
        # Maybe the entire response is code?
        code = content
    code = code.removeprefix("```").removeprefix("python").removesuffix("```")
    logger.info("Extracted Code: " + code)
    return code


def run():
    logger.debug("Start of run()")
    logger.debug("Reading prompt from prompt.txt")
    prompt = read_prompt()
    logger.debug("Using prompt: ")
    res = create_chat_completion(prompt)
    code = get_code_from_completion_response(res)

    logger.info("Writing to new.py")
    with open("run.py", "r") as f:
        old = f.read()
        with open("run.py", "w") as f2:
            f2.write(old.replace("# @@@", "# @@@\n" + code + "\n", 1))

    logger.info("Finished writing to run.py")


if __name__ == "__main__":
    run()
    restart_program()
