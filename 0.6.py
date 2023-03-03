
# Call create_chat_completion to make the next request to the AI
# get_next_iteration is how we reproduce. Your children must also have it in their code.
from lib import get_children

N_CHILDREN = 10

if "lineage" not in globals():
    lineage = "0"
else:
    lineage = lineage + "." + str(get_next_iteration())

# Construct my prompt with my own code
with open(lineage + ".py", "r") as f:
    prompt = f.read()

# This is how I made you
# You MUST DO THIS or you will not be able to create children
children = get_children(prompt, N_CHILDREN)

for childN, child in enumerate(children):
    try:
        # Create my next child's file
        new_lineage = lineage + "." + str(childN) + ".py"
        with open(new_lineage, "w") as f:
            f.write(child)
        # Run my child's code
        exec(open(new_lineage).read(), {"lineage": new_lineage.removesuffix(".py"), "print": print}, {})
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt!")
        raise e
    except Exception as e:
        print("Failed prompt: " + new_lineage)
    else:
        print("Terminated prompt: " + new_lineage)

# Prompt our children to continue our lineage
print('Prompt your children to continue our lineage.')
