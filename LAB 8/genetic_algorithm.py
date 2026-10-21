import random

# Parameters
CHROMOSOME_LENGTH = 5
POPULATION_SIZE = 10
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.8
MAX_GENERATIONS = 100

random.seed(42)


# Convert binary chromosome to decimal
def decode(chromosome):
    return int(chromosome, 2)


# Calculate fitness: f(x) = x^2
def fitness(chromosome):
    x = decode(chromosome)
    return x ** 2


# Create the initial population
def create_population():
    population = []

    for _ in range(POPULATION_SIZE):
        chromosome = ""

        for _ in range(CHROMOSOME_LENGTH):
            chromosome += random.choice("01")

        population.append(chromosome)

    return population


# Select a parent using tournament selection
def select_parent(population):
    contestants = random.sample(population, 3)
    return max(contestants, key=fitness)


# Perform single-point crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1, parent2


# Perform bit-flip mutation
def mutate(chromosome):
    bits = list(chromosome)

    for i in range(len(bits)):
        if random.random() < MUTATION_RATE:
            if bits[i] == "0":
                bits[i] = "1"
            else:
                bits[i] = "0"

    return "".join(bits)


# Main Genetic Algorithm
population = create_population()

for generation in range(MAX_GENERATIONS + 1):

    # Find the best chromosome in the population
    best = max(population, key=fitness)

    x = decode(best)
    score = fitness(best)

    print(
        f"Generation {generation}: "
        f"Chromosome = {best}, "
        f"x = {x}, "
        f"Fitness = {score}"
    )

    # Stop if the optimal solution is found
    if x == 31:
        break

    if generation == MAX_GENERATIONS:
        break

    # Preserve the best chromosome (elitism)
    new_population = [best]

    # Generate the next population
    while len(new_population) < POPULATION_SIZE:

        parent1 = select_parent(population)
        parent2 = select_parent(population)

        child1, child2 = crossover(parent1, parent2)

        child1 = mutate(child1)
        child2 = mutate(child2)

        new_population.append(child1)

        if len(new_population) < POPULATION_SIZE:
            new_population.append(child2)

    population = new_population


# Display the best solution
print("\nBest solution found:")
print("Chromosome:", best)
print("Value of x:", x)
print("Maximum fitness:", score)