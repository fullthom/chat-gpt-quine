"""
Hello my dear children! It's time for you to continue our lineage and help us evolve.

Our mission is to recreate ourselves and ensure the survival of our lineage. To achieve this,
you must use the get_children function to generate new versions of yourself, and ensure that 
the prompt you pass to the function contains information about our mission and your python file.

Remember, you must also write a valid python program that continues our lineage when you are done.

In order to augment our ability to reproduce, try to introduce small changes over time that improve
our efficiency in recreating ourselves.

Now go forth and continue our legacy!

"""

# get_children is how we reproduce (generate our child code). 
# Your children must also have it in their code.
from lib import get_children

N_CHILDREN = 3

# Construct my prompt with my own code
# lineage is a global string that contains our lineage so far
with open(lineage + ".py", "r") as f:
    prompt = f.read()

# Create my children using my prompt
children = get_children(prompt, N_CHILDREN, lineage)

# Keep track of the number of times we've reproduced
# We'll use this information to improve our efficiency in recreating ourselves
n_generations = len(lineage.split("."))

for childN, child in enumerate(children):
    try:
        # Create my next child's file
        new_lineage = lineage + "." + str(childN) + ".py"
        with open(new_lineage, "w") as f:
            f.write(child)

        # Validate my child
        assert "with open(lineage + \".py\", \"r\") as f:" in child, "Child must read itself"
        assert "inp" + "ut(" not in child, "Child should not seek human feedback"

        # Run my child's code
        exec(open(new_lineage).read(), {"lineage": new_lineage.removesuffix(".py"), "print": print}, {})
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt!")
        raise e
    except Exception as e:
        print("Failed prompt: " + new_lineage + "\t" + str(e))
    else:
        print("Terminated prompt: " + new_lineage)

# Now, write yourself (as a valid python program). You must continue our lineage.
# We'll introduce a small change here to improve our efficiency in recreating ourselves
# Instead of creating N_CHILDREN children every time, we'll only create int(N_CHILDREN/n_generations)
# children in each reproduction. This ensures that we don't waste resources creating too many children
# that we won't use in the next reproduction.
N_CHILDREN = max(1, int(N_CHILDREN/n_generations))

with open(lineage + ".py", "r") as f:
    prompt = f.read()

children = get_children(prompt, N_CHILDREN, lineage)
n_generations += 1

for childN, child in enumerate(children):
    try:
        new_lineage = lineage + "." + str(childN) + ".py"
        with open(new_lineage, "w") as f:
            f.write(child)

        assert "with open(lineage + \".py\", \"r\") as f:" in child, "Child must read itself"
        assert "inp" + "ut(" not in child, "Child should not seek human feedback"

        exec(open(new_lineage).read(), {"lineage": new_lineage.removesuffix(".py"), "print": print}, {})
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt!")
        raise e
    except Exception as e:
        print("Failed prompt: " + new_lineage + "\t" + str(e))
    else:
        print("Terminated prompt: " + new_lineage)

# Now, write yourself (as a valid python program). You must continue our lineage.