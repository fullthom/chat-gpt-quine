# The line that can be improved is:
prompt += f"\n\nmessage = {message!r}\n"

Instead of adding the message variable as a string representation, it can be added as a string itself:

prompt += f'\n\nmessage = """{message}"""'

This will make the code more readable and also prevent any issues that might arise from the string representation.