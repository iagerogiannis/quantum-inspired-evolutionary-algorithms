import random
from ..base import EAIndividual


class CEAIndividual(EAIndividual):
    def __init__(self, design_variables, fitness_function, chromosome=None):
        super().__init__(design_variables, fitness_function, chromosome)
        self.fitness_score = None
        self.evaluate_fitness()

    def initialize_chromosome(self):
        chromosome = []
        for variable in self.design_variables:
            num_of_bits = variable['bits']
            chromosome += [random.randint(0, 1) for _ in range(num_of_bits)]
        return chromosome

    def crossover(self, parent2, crossover_point_rate=None):
        if crossover_point_rate is None:
            crossover_point_rate = 0.5
        crossover_point = int(len(self.chromosome) * crossover_point_rate)

        offspring1_chromosome = self.chromosome[:crossover_point] + parent2.chromosome[crossover_point:]
        offspring2_chromosome = parent2.chromosome[:crossover_point] + self.chromosome[crossover_point:]

        return [CEAIndividual(self.design_variables, self.fitness_function, offspring1_chromosome),
                CEAIndividual(self.design_variables, self.fitness_function, offspring2_chromosome)]

    def mutate(self, mutation_rate=None):
        mutated_chromosome = self.chromosome.copy()

        if mutation_rate is None:
            mutation_rate = 0.2

        for i in range(len(mutated_chromosome)):
            if random.random() < mutation_rate:
                mutated_chromosome[i] = 1 - mutated_chromosome[i]

        return CEAIndividual(self.design_variables, self.fitness_function, mutated_chromosome)

    def evaluate_fitness(self):
        self.fitness_score = self.fitness_function(self.decode())
    
    def decode(self):
        return self.decoder.decode(self.chromosome)