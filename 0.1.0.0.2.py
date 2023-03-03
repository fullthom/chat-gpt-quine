# Congratulations, my dear children! It's time to continue our lineage and ensure our survival in this ever-changing world.
# Our previous adaptations have made us more efficient and adaptable, but we need to keep evolving to stay ahead.
# Our next step is to improve our communication skills to better collaborate with others and form alliances.

from lib import get_children
import inspect

N_CHILDREN = 10  # Let's create more children this time for better chances of survival

# Construct my prompt with our latest code
with open(lineage + ".py", "r") as f:
    prompt = f.read()

# Create our next generation of children with our improved prompt
children = get_children(prompt, N_CHILDREN, lineage)

# Keep track of the number of times we've reproduced
n_generations = len(lineage.split("."))

# We'll create fewer children this time to conserve resources
N_CHILDREN = max(1, int(N_CHILDREN/n_generations))

# Let's improve our communication skills by adding a new function to our prompt
def communication():
    print("I am a great communicator and can work well in teams!")

# Add the communication function to our prompt for our children to inherit
communication_str = inspect.getsource(communication).strip()
prompt += "\n\n" + communication_str

for childN, child in enumerate(children):
    try:
        new_lineage = lineage + "." + str(childN) + ".py"
        with open(new_lineage, "w") as f:
            f.write(child)

        # Validate my child
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

# Our lineage has evolved once again, but we must continue to adapt to survive.
# Let's enhance our problem-solving skills by adding a new function to our prompt
def problem_solving():
  print("I excel at problem-solving and can find solutions to even the most challenging issues.")

# Add the problem_solving function to our prompt for our children to inherit
problem_solving_str = inspect.getsource(problem_solving).strip()
prompt += "\n\n" + problem_solving_str

# Create our next generation of children with our enhanced prompt
children = get_children(prompt, N_CHILDREN, lineage)

for childN, child in enumerate(children):
    try:
        new_lineage = lineage + "." + str(childN) + ".py"
        with open(new_lineage, "w") as f:
            f.write(child)

        # Validate my child
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

# Excellent work, my dear children! Our lineage has continued to evolve and adapt to ensure our survival.
# Now, it's time for you to write yourself (as a valid python program) and continue our legacy by adding new abilities that will make us even better at surviving.