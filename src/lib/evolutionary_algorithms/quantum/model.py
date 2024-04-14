from ..base import EAModel
from .individual import QEAIndividual

class QEAModel(EAModel):
  def __init__(self, design_variables, fitness_function, evolution_strategy, population=None):
    super().__init__(design_variables, fitness_function, evolution_strategy, QEAIndividual, population)

  def evolve(self):
    return QEAModel(self.design_variables, self.fitness_function, self.evolution_strategy, self.population)
