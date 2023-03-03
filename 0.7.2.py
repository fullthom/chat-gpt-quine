# Prompt my own children with the message
for childN in range(N_CHILDREN):
    exec(f"print({childN})")
    try:
        exec(f"print({lineage}.{childN}.message)")
    except AttributeError:  # The child may have crashed before the message was created
        pass

print("All prompts complete. Continuing to next iteration.")