from ..chromosome_decoder import ChromosomeDecoder

class EAIndividual:
    def __init__(self, design_variables, fitness_function, chromosome=None):
        self.design_variables = design_variables
        self.fitness_function = fitness_function
        self.decoder = ChromosomeDecoder(design_variables)
        self.chromosome = chromosome if chromosome else self.initialize_chromosome()