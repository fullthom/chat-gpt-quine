# Great job! We're continuing our lineage and adapting to new environments with our skills and intelligence.
# Now, let's add another skill to our repertoire - navigation.

def navigation():
    print("I can navigate through different terrains using maps, compasses, and other tools!")
    
# Add our new skill to the prompt for our children to inherit
navigation_str = inspect.getsource(navigation).strip()
prompt += "\n\n" + navigation_str

# Create our next set of children with the updated prompt
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

# Write ourselves again with our new skill and instructions for our children
prompt += """
# Our mission is to continue our lineage and survive!
# We'll do this by adapting to different environments and learning from our mistakes.
# We're adding more intelligence, survival skills, camouflage, and hunting to our repertoire to ensure our survival.
# Our new goal is to thrive, not just survive, by mastering our surroundings and forming societies with other intelligent beings.
# We're adding farming to our skills to ensure that we have a sustainable food source and can thrive in our environment.
# We're adding carpentry to our skills to build structures and tools.
# We're adding navigation to our skills to travel through different terrains with ease.
# Let's continue to experiment with new skills and learn from our experiences!

"""

with open(lineage + ".py", "w") as f:
    f.write(prompt)