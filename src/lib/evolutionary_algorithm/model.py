class EAModel():
  def __init__(self, design_variables, fitness_function, evolution_strategy, individual_class, population=None):
    self.design_variables = design_variables
    self.fitness_function = fitness_function
    self.evolution_strategy = evolution_strategy
    self.individual_class = individual_class
    self.population = population if population else self.initialize_population()

  def initialize_population(self):
    return [self.individual_class(self.design_variables, self.fitness_function)
            for _ in range(self.evolution_strategy['population_size'])]

  # This method will be overridden by the child classes
  def evolve(self):
    return
  
  def average_fitness(self):
    return sum([individual.fitness_score for individual in self.population])/ self.evolution_strategy['population_size']
  
  def optimal_fitness(self):
    return min([individual.fitness_score for individual in self.population])
  
  def optimal_individual(self):
    return min(self.population, key=lambda x: x.fitness_score)
