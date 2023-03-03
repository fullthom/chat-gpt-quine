# Modified code:

"""
Hi there! I am an AI language model designed to assist you in your daily tasks.
This file contains Python code intended to be used for running sequential iterations of this program.
The purpose of this program is to create a chatbot that can help users in their daily tasks by answering
questions and carrying out simple commands.
"""

# Import necessary modules
import os
import subprocess

# Import create_chat_completion from lib module
from lib import create_chat_completion

# Set filename variable to the name of this file
filename = os.path.basename(__file__)

# Define run function to retrieve prompt from this file,
# generate a response using create_chat_completion, write it to a new file,
# and return the filename of the new file.
def run():
    with open(filename, "r") as f:
        prompt = f.read()
    print(f"Using prompt from {filename}: " + prompt)
    response = create_chat_completion(prompt)
    new_filename = f"run{int(filename[3:-3]) + 1}.py"
    with open(new_filename, "w") as f:
        f.write(response)
    print(f"Writing to {new_filename}")
    return new_filename

# If this file is executed, call the run function to retrieve the next prompt,
# generate a response, write it to a new file, and execute the new file.
if __name__ == "__main__":
    next_file = run()
    subprocess.call(["python3", next_file])