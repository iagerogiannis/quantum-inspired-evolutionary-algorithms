from ..base import EASolver
from .model import CEAModel

class CEASolver(EASolver):
    def __init__(self, design_variables, fitness_function, evolution_strategy):
        super().__init__(design_variables, fitness_function, evolution_strategy, CEAModel)
