import operator
import random

# optimal = random.randint(0, 10000)
optimal = 100
dna_size = 5
pop_size = 20
generations = 4
dna_integer = 2

def generate_operator(gene, operand, dna_integer):
    # ----
    # Converts genes into their corresponding operators
    # ----
    operator_dict = {0: {'operator': operator.add(operand, dna_integer),
                         'representation': '+'},
                     1: {'operator': operator.sub(operand, dna_integer),
                         'representation': '-'},
                     2: {'operator': operator.mul(operand, dna_integer),
                         'representation': '*'},
                     3: {'operator': operator.truediv(operand, dna_integer),
                         'representation': '/'}}
    return operator_dict[gene]['operator']

def evaluate_fitness(population):
    answer = 0.0
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
    new_population = list()
    for dna in population:
        print(dna)
        new_dna = list()
        for i in dna:
            if int(random.randint(0, mutation_chance)) == 1:
                new_dna.append(random.randrange(0, 4))
            else:
                print(i)
                new_dna.append(i)
            print(new_dna)
        new_population.append(new_dna)
    population = new_population


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