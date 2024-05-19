import os
import matplotlib.pyplot as plt


class EASolver():
  def __init__(self, design_variables, fitness_function, evolution_strategy, model):
    self.model = model(
      design_variables,
      fitness_function,
      evolution_strategy,
    )
    self.num_of_generations = evolution_strategy['num_of_generations']
    self.generations = [self.get_current_generation()]

  def get_current_generation(self):
    return {
      'opt_solution': self.model.get_optimal_solution(),
      'opt_fitness': self.model.get_optimal_fitness(),
      'avg_fitness': self.model.get_average_fitness(),
    }
  
  def solve(self):
    for _ in range(self.num_of_generations - 1):
      self.model.evolve()
      self.generations.append(self.get_current_generation())

  def print_solution_summary(self):
    print(f'Optimal Solution: {self.generations[-1]["opt_solution"]}')
    print(f'Optimal Fitness: {self.generations[-1]["opt_fitness"]}')
    print(f'Average Fitness: {self.generations[-1]["avg_fitness"]}')

  def plot_convergence(self, filename='convergence.png'):
    def get_optimal_fitness(i):
      return self.generations[i]['opt_fitness']

    convergence = [
      get_optimal_fitness(i) for i in range(len(self.generations))
    ]

    if not os.path.exists('results'):
      os.makedirs('results')

    plt.clf()
    plt.plot(range(len(convergence)), convergence)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Convergence of Generations')
    plt.savefig(f'results/{filename}')
