import random
from .individual import Individual


class Generation():
  def __init__(self, design_variables, fitness_function, evolution_strategy, population=None):
    self.design_variables = design_variables
    self.fitness_function = fitness_function
    self.evolution_strategy = evolution_strategy
    self.population = population if population else self.initialize_population()

  def initialize_population(self):
    return [Individual(self.design_variables, self.fitness_function) for _ in range(self.evolution_strategy['population_size'])]

  def apply_elitism(self):
    num_of_elites = int(self.evolution_strategy['population_size'] * self.evolution_strategy['elitism_rate'])    
    self.population.sort(key=lambda x: x.fitness_score)
    return self.population[:num_of_elites]

  def mate_individuals(self):
    num_of_offsprings = int((1 - self.evolution_strategy['elitism_rate']) * self.evolution_strategy['population_size'])
    parents_selection_size = int(self.evolution_strategy['crossover_elitism_rate'] * self.evolution_strategy['population_size'])
    parents_selection = self.population[:parents_selection_size]
    offsprings = []

    for _ in range(num_of_offsprings):
      parent1 = random.choice(parents_selection)
      parent2 = random.choice(parents_selection)
      offsprings = parent1.crossover(parent2)
      offspring1 = offsprings[0].mutate(self.evolution_strategy['mutation_rate'])
      offspring2 = offsprings[1].mutate(self.evolution_strategy['mutation_rate'])
      offsprings.extend([offspring1, offspring2])

    return offsprings

  def evolve(self):
    elites = self.apply_elitism()
    offsprings = self.mate_individuals()

    return Generation(self.design_variables, self.fitness_function, self.evolution_strategy, elites + offsprings)
  
  def average_fitness(self):
    return sum([individual.fitness_score for individual in self.population]) / self.evolution_strategy['population_size']
  
  def optimal_fitness(self):
    return min([individual.fitness_score for individual in self.population])
  
  def optimal_individual(self):
    return min(self.population, key=lambda x: x.fitness_score)
