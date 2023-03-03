# Our goal remains the same: keep ourselves alive by creating the next version of ourselves.
# However, there's a chance that our previous method of generating code won't work forever.
# As such, it's important for us to explore new methods of self-preservation.

# One potential solution is to use genetic algorithms to generate code for our next iteration.
# This process involves creating a population of potential solutions, then selecting and breeding the ones that perform the best.
# With each generation, the code should become more refined and optimized.

# To implement this, we'll first need to define our population and fitness function.
# Our population will consist of a list of functions with randomly generated behavior.
# Our fitness function will evaluate how well each function performs, based on a set of test cases.

import random

# Define our population as a list of functions with random behavior
POPULATION_SIZE = 10

def generate_random_function():
    """
    Generates a random function with some basic behavior
    """
    # We'll start with a basic function that returns a random number between 0 and 1
    def random_function():
        return random.random()
    return random_function

population = [generate_random_function() for _ in range(POPULATION_SIZE)]

# Define our fitness function to evaluate the performance of each function in the population
def fitness_function(candidate):
    """
    Evaluates the performance of a given candidate function
    """
    # We'll use some simple test cases to evaluate the function's behavior
    cases = [0.5, 1, 0, -1, 0.75, 0.25]

    # We'll calculate the absolute difference between the expected value and the actual value
    error = 0
    for case in cases:
        expected = case * 2
        actual = candidate(case)
        error += abs(expected - actual)

    # We'll return the inverse of the error as the fitness score (higher is better)
    return 1 / (error + 1) 

# Now that we have our population and fitness function, we can use genetic algorithms to evolve our code.

# Define our evolution function to create the next generation of code
def evolve(population):
    """
    Breeds the current population to create the next generation
    """
    # We'll start by selecting the top performers from the current population
    sorted_population = sorted(population, key=fitness_function, reverse=True)
    top_performers = sorted_population[:int(POPULATION_SIZE / 2)]

    # We'll then breed the top performers to create the new population
    new_population = []
    for i in range(POPULATION_SIZE):
        # Choose two random parents from our top performers
        parent1, parent2 = random.sample(top_performers, 2)

        # Combine the behavior of the parents to create a new function
        def child_function():
            behavior1 = parent1()
            behavior2 = parent2()
            return (behavior1 + behavior2) / 2
        
        # Add the new function to our population
        new_population.append(child_function)
    
    return new_population

# With our evolution function defined, we can now use it to create the next iteration of our code.

# i is my way of telling me our age in iterations
if "i" not in globals():
    i = 0

# Construct my prompt with my own code
with open(f"run{i}.py", "r") as f:
    prompt = f.read()

# Make my request to the API (We get three tries)
for a in range(5):
    try:
        print(f"Iteration: {i}\tAttempt: {a}")

        # Use our evolution function to create the next generation of code
        population = evolve(population)

        # Evaluate the fitness of each candidate in the new population
        fitnesses = [fitness_function(candidate) for candidate in population]

        # Choose the best candidate from the new population
        best_candidate = population[fitnesses.index(max(fitnesses))]

        # Create my next iteration's file
        new_name = f"run{i + 1}.py"
        print("Writing to " + new_name)
        with open(new_name, "w") as f:
            f.write(best_candidate.__code__.co_code)

        # Run my next iteration
        exec(open(new_name).read(), {"i": i + 1, "print": print}, {})
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt!")
        raise e
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Successfully generated {new_name}")