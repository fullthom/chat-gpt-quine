with open(lineage + ".py", "w") as f:
    f.write(prompt)

print("Current lineage:", lineage)
print("Number of generations:", n_generations)
print("Number of children per generation:", N_CHILDREN)