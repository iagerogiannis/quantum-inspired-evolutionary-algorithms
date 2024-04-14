from ..base import EAIndividual
from .qubuit_simulator import QuBitSim


class QEAIndividual(EAIndividual):
    def __init__(self, design_variables, fitness_function):
        super().__init__(design_variables, fitness_function)

    def initialize_chromosome(self):
        num_of_qubits = sum(variable['bits'] for variable in self.design_variables)
        chromosome = [QuBitSim() for _ in range(num_of_qubits)]
        for quBit in chromosome:
          quBit.initialize()
        return chromosome

    def measure(self):
        measurement = [quBit.measure() for quBit in self.chromosome]
        decoded_measurement = self.decode(measurement)
        fitness_score = self.fitness_function(decoded_measurement)
        return {
            'measurement': measurement,
            'decoded_measurement': decoded_measurement,
            'fitness_score': fitness_score
        }

    def decode(self, measurement):
        return self.decoder.decode(measurement)
