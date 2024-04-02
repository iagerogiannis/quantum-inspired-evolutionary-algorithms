from ..chromosome_decoder import ChromosomeDecoder
from .qubuit_simulator import QuBitSim


class QuantumIndividual():
    def __init__(self, design_variables, fitness_function):
        self.design_variables = design_variables
        self.fitness_function = fitness_function
        self.decoder = ChromosomeDecoder(design_variables)
        self.chromosome = self.initialize_chromosome()

    def initialize_chromosome(self):
        num_of_qubits = sum(variable['bits'] for variable in self.design_variables)
        chromosome = [QuBitSim() for _ in range(num_of_qubits)]
        for quBit in chromosome:
          quBit.initialize()
        return chromosome

    def measure(self):
        measurement = [quBit.measure() for quBit in self.chromosome]
        print(measurement)
        decoded_measurement = self.decode(measurement)
        fitness_score = self.fitness_function(decoded_measurement)
        return {
            'measurement': measurement,
            'decoded_measurement': decoded_measurement,
            'fitness_score': fitness_score
        }

    def decode(self, measurement):
        return self.decoder.decode(measurement)
