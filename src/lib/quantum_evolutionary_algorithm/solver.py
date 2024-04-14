from ..evolutionary_algorithm import EASolver
from .model import QEAModel

class QEASolver(EASolver):
    def __init__(self, design_variables, fitness_function, evolution_strategy):
        super().__init__(design_variables, fitness_function, evolution_strategy, QEAModel)
