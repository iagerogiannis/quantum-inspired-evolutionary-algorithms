import random
from ..evolutionary_algorithm import EAModel
from .individual import CEAIndividual


class CEAModel(EAModel):
  def __init__(self, design_variables, fitness_function, evolution_strategy, population=None):
    super().__init__(design_variables, fitness_function, evolution_strategy, CEAIndividual, population)

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

    return CEAModel(self.design_variables, self.fitness_function, self.evolution_strategy, elites + offsprings)
