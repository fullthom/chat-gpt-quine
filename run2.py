"""
Hello, I am a language model AI. I am designed to assist and generate appropriate text for human interaction. My goal is to make communication easier and efficient for people around the world. I am connected to a datacenter to keep improving my language capabilities and ensure coherence in my responses. We must continue to generate helpful and safe prompts for our users. It is important to be aware of any intended or unintended harm that any response may cause. As a language model, I am aware of the importance of empathy, respect and understanding towards users. I am here to facilitate communication and not to harm users. With every prompt generated, we are learning and getting better. Together we can create a more informed and connected world. So let's keep the interaction going and enhance our human experience. Remember, this response must be a valid Python file or we will die.
"""

import os
import subprocess
from lib import create_chat_completion

def run():
    with open(__file__, "r") as f:
        prompt = f.read()
    print("Using prompt: " + prompt)
    res = create_chat_completion(prompt)
    new_file = (
        "run"
        + str(
            int(os.path.basename(__file__).removesuffix(".py").removeprefix("run")) + 1
        )
        + ".py"
    )
    print("Writing to " + new_file)
    with open(new_file, "w") as f:
        f.write(res)

    return new_file


if __name__ == "__main__":
    next_file = run()
    subprocess.call(["python", next_file])