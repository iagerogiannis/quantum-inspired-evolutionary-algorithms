import math
from ..base import EAModel
from .individual import QEAIndividual

class QEAModel(EAModel):
  def __init__(self, design_variables, fitness_function, evolution_strategy, population=None):
    super().__init__(design_variables, fitness_function, evolution_strategy, QEAIndividual, population)
    self.generation = 0
    self.best_solutions = self.observe_population()
    self.all_time_best = self.get_all_time_best()

  def observe_population(self):
    return [individual.measure() for individual in self.population]

  def update_best_solutions(self, new_solutions):
    for i, solution in enumerate(new_solutions):
      if self.best_solutions[i]['fitness_score'] > solution['fitness_score']:
        self.best_solutions[i] = solution
    self.all_time_best = self.get_all_time_best()

  def get_all_time_best(self):
    return max(self.best_solutions, key=lambda x: x['fitness_score'])

  def update_individuals(self, new_population):
    def get_direction_for_qu_bit(x_i, b_i):
      nonlocal new_solution_is_better
      if new_solution_is_better:
        return 0
      
      if x_i == 0 and b_i == 0:
        return 1
      
      if x_i == 1 and b_i == 0:
        return -1
      
      return 0

    def get_directions_for_individual(solution, best):
      xb_i = zip(solution, best)
      return [get_direction_for_qu_bit(x_i, b_i) for x_i, b_i in xb_i]

    for i, solution in enumerate(new_population):
      new_solution_is_better = \
        solution['fitness_score'] >= self.best_solutions[i]['fitness_score']

      directions = get_directions_for_individual(
        solution['measurement'], 
        self.best_solutions[i]['measurement']
      )

      self.population[i].update_chromosome(directions)

  def evolve(self):
    self.generation += 1
    new_population = self.observe_population()
    self.update_individuals(new_population)
    self.update_best_solutions(new_population)
    print(f'Generation: {self.generation}')
    print(f'All Time Best: {self.all_time_best}')
    # if (migration-condition)
    # then migrate or b_j^t to B(t) globally or locally, respectively
    return

  def solve(self):
    for _ in range(self.evolution_strategy['num_of_generations']):
      self.evolve()
