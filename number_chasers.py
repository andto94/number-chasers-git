import operator
import random

# optimal = random.randint(0, 10000)
optimal = 5000
dna_size = 20
pop_size = 20
generations = 200
dna_integer = 5

def generate_operator(gene, answer, dna_integer):
    # ----
    # Converts genes into their corresponding operators
    # ----
    a = answer
    b = dna_integer
    operator_dict = {0: {'operator': operator.add(a, b),
                         'representation': '+'},
                     1: {'operator': operator.sub(a, b),
                         'representation': '-'},
                     2: {'operator': operator.mul(a, b),
                         'representation': '*'},
                     3: {'operator': operator.floordiv(a, b),
                         'representation': '/'}}
    return operator_dict[gene]['operator']

def evaluate_fitness(population):
    answer = 0
    fitness_values = list()
    for dna in population:
        for i in dna:
            answer = generate_operator(i, answer, dna_integer)
            if abs(answer) < optimal:
                answer = abs(answer) - optimal
            else:
                answer = optimal - abs(answer)
        fitness_values.append(answer)

    return fitness_values

def init_population(dna_size, pop_size):
    # ----
    # Randomly generates a population of lists containing integers
    # 0, 1, 2, or 3.
    # ----
    population = list()
    for pop_member in range(pop_size):
        dna_strand = list()
        for gene_member in range(dna_size):
            gene = random.randrange(0, 4)
            dna_strand.append(gene)
        population.append(dna_strand)

    return population

def mutate(population):
    # ----
    # Each gene in the DNA sequence has a 1/(mutation_chance) to be
    # swapped out with a random operator to encourage diversity in
    # the gene pool.
    # ----
    mutation_chance = 50
    new_dna = list()
    for dna in population:
        for i in dna:
            if int(random.random()*mutation_chance) == 1:
                new_dna = random.randrange(0, 4)
            else:
                new_dna = dna[i]

    return population

def selection(population, fitness_values):
    ranks = sorted(zip(fitness_values, population))
    n = len(fitness_values)
    rank_sum = n*(n+1)//2
    weight = list()
    for rank in range(n):
        weight.append(rank / rank_sum)
    selected = random.choices(ranks, weights=weight, k=10)
    selected_fitness, selected = list(zip(*selected))
    return selected

def recombine(parents):
    # Crossover recombination
    offspring = list()
    number_of_offspring = 0
    while number_of_offspring < (dna_size - len(parents)):
        dna_strand1, dna_strand2 = random.choices(parents, k=2)
        crossover_point = random.randrange(dna_size)
        offspring.append(dna_strand1[:crossover_point] +
                         dna_strand2[crossover_point:])
        offspring.append(dna_strand2[:crossover_point] +
                         dna_strand1[crossover_point:])
        number_of_offspring += 2

    return list(parents) + offspring


population = init_population(dna_size, pop_size)
fitness_values = evaluate_fitness(population)


current_generations = 0
while (current_generations != generations):
    survivors = selection(population, fitness_values)
    next_generation = recombine(survivors)
    next_generation = mutate(next_generation)
    fitness_values = evaluate_fitness(next_generation)
    # population = selection(next_generation, fitness_values)
    population = next_generation
    current_generations += 1
    tmp = set()
    # for dna in population:
    #     tmp.add(tuple(dna))
    # if ((len(tmp) == 1) == True):
    #     break
    print(current_generations)

final_generation = sorted(zip(fitness_values, population))
print(*final_generation, sep='\n')