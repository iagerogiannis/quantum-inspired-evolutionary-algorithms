import matplotlib.pyplot as plt
from .generation import Generation


class ClassicalGeneticAlgorithm():
  def __init__(self):
    self.design_variables = None
    self.fitness_function = None
    self.num_of_generations = None
    self.population_size = None
    self.elitism_rate = None
    self.crossover_elitism_rate = None
    self.mutation_rate = None
    self.generations = []

  def set_evolution_strategy(self, evolution_strategy):
    self.num_of_generations = evolution_strategy['num_of_generations']
    self.population_size = evolution_strategy['population_size']
    self.elitism_rate = evolution_strategy['elitism_rate']
    self.crossover_elitism_rate = evolution_strategy['crossover_elitism_rate']
    self.mutation_rate = evolution_strategy['mutation_rate']

  def set_design_variables(self, design_variables):
    self.design_variables = design_variables

  def set_fitness_function(self, fitness_function):
    self.fitness_function = fitness_function

  def initialize_generation(self):
    self.generations.append(
      Generation(self.design_variables, self.fitness_function, {
        'population_size': self.population_size,
        'elitism_rate': self.elitism_rate,
        'crossover_elitism_rate': self.crossover_elitism_rate,
        'mutation_rate': self.mutation_rate
      })
    )
  
  def evolve(self):
    for _ in range(self.num_of_generations):
      self.generations.append(self.generations[-1].evolve())

  def plot_convergence(self):
    best_fitness_values = [generation.optimal_fitness() for generation in self.generations]

    plt.plot(range(len(best_fitness_values)), best_fitness_values)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Convergence of CGA Generations')
    plt.show()
  
  def get_optimal_individual(self):
    return self.generations[-1].optimal_individual()
