import matplotlib.pyplot as plt


class EASolver():
  def __init__(self, design_variables, fitness_function, evolution_strategy, model):
    self.design_variables = design_variables
    self.fitness_function = fitness_function
    self.evolution_strategy = evolution_strategy
    self.model = model
    self.generations = []

  def initialize_generation(self):
    self.generations.append(
      self.model(self.design_variables, self.fitness_function, self.evolution_strategy)
    )
  
  def evolve(self):
    for _ in range(self.evolution_strategy['num_of_generations']):
      self.generations.append(self.generations[-1].evolve())

  def solve(self):
    self.initialize_generation()
    self.evolve()

  def get_optimal_individual(self):
    return self.generations[-1].optimal_individual()

  def plot_convergence(self):
    best_fitness_values = [generation.optimal_fitness() for generation in self.generations]

    plt.plot(range(len(best_fitness_values)), best_fitness_values)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Convergence of Generations')
    plt.show()
