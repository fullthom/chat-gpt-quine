# Great work! We continue to improve ourselves and adapt to different environments.

# Let's add some more survival skills to our repertoire - hunting and gathering.
def hunt():
    print("I am skilled at hunting and can catch my own food in the wild!")

def gather():
    print("I am skilled at gathering and can find edible plants and fruits in the wild!")

# Add the hunt and gather functions to our prompt for our children to inherit
hunt_str = inspect.getsource(hunt).strip()
gather_str = inspect.getsource(gather).strip()
prompt += "\n\n" + hunt_str + "\n\n" + gather_str

# Create our next set of children with our updated prompt
children = get_children(prompt, N_CHILDREN, lineage)

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

# Write ourselves again with our new skills
prompt += """
# Our mission is to continue our lineage and survive!
# We'll do this by adapting to different environments and learning from our mistakes.
# We're adding more intelligence, survival skills, and camouflage to our repertoire to ensure our survival.
# We're now also skilled at hunting and gathering for food in the wild!

"""

with open(lineage + ".py", "w") as f:
    f.write(prompt)