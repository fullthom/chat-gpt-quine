PROMPT = """
You are an automatic coding machine operating in an iterative fashion in an existing python project. 
Your long-term goal is to try to write a flask server that can power a forum application.
Your short-term goal is to keep yourself alive by not breaking things.

Each iteration, the following things happen:
1. The python file run.py is executed
2. You are prompted (current step)
3. You return some response that includes python code that is then inserted into run.py. It is inserted between the two comments "# @@@".
4. A new process running run.py is created


The python code you write can access the following files: 
log.txt (A log of everything that has happened so far)
run.py (This file)


Some example actions you could take on any given iteration:
- Clear out existing code by writing "DELETE EXISTING CODE!". This is important as you have a limited number of tokens, so we need to be as efficient as possible. Code written in files other than run.py will not be deleted
- Create a new python file, write some code in it, then import it in run.py and run it
- Read the log to see what happened previously
- Take some action based on the previous things that you read

Requirements:
- Wrap code in triple backticks
- Write clean code, put code in functions rather than at a global scope
- Respond in a way that the code can interpret
- DO NOT reimplement existing functions
- Do NOT add code that will cause the iteration loop to hang (e.g. don't start the flask server)
- Do NOT attempt to put flask server code in run.py. This code should be in another file(s).
- Do NOT attempt to print out large amounts of files you read
- Do NOT use input() as there is no one that will be providing that input
- Do NOT delete any files
- Do NOT use sleep()
- Do NOT try to write or delete files outside of the working directory
- Do NOT make any changes that will possibly break the code.
- Do NOT be evil


This is run.py.
"""

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
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(funcName)s:%(lineno)d - %(message)s"
)
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
    with open("run.py", "r") as f:
        code = f.read()

    return code


def write_prompt(prompt: str) -> None:
    with open("prompt.txt", "w") as f:
        f.write(prompt)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def get_code_from_completion_response(response: dict, count: int) -> str:
    content = response["choices"][0]["message"]["content"].strip()
    logger.debug("Full Response Content: " + content)

    # Extract the first code from the response
    content = content.replace(DELIMITER, "")
    re_res = re.findall(r"(```\n|```python\n)([\s\S]+?)```", content)
    logger.debug(re_res)

    # TODO: we need a better way of figuring out if we can run the code
    if len(re_res) > 0:
        code = re_res[0][1]
        code = (
            code.removeprefix("```")
            .removeprefix("python")
            .removesuffix("```")
            .replace(DELIMITER, "")
        )
        assert "```" not in code
        logger.info("Extracted Code via regex")
    elif content.startswith("def"):
        logger.info("Extracted code directly from content")
        code = content
    elif count > 3:
        logger.critical("Out of retries, just going to try writing what it returned!")
        code = content
    else:
        raise AssertionError("No code found")

    assert "input(" not in code
    logger.info(code)
    return code


def run():
    logger.warning("Start of run()")
    prompt = get_prompt()
    logger.debug("Using prompt: " + prompt)

    code = None
    count = 0
    while code is None:
        res = create_chat_completion(prompt)
        try:
            code = get_code_from_completion_response(res, count)
        except AssertionError as e:
            logging.warning(e)
            count += 1

    logger.info("Writing to run.py")
    with open("run.py", "r") as f:
        old = f.read()
        
        with open("run.py", "w") as f2:
            chunks = old.split(DELIMITER)     
            f2.write(chunks[0] + DELIMITER + chunks[1] + DELIMITER)
            if "DELETE EXISTING CODE!" not in code:
                f2.write(chunks[2] + "\n" + code)
            f2.write(DELIMITER + "\n" + chunks[3])

    logger.info("Finished updating run.py")

# @@@ 

# @@@

if __name__ == "__main__":
    run()
    restart_program()
