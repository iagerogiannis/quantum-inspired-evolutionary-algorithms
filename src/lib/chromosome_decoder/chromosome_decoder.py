class ChromosomeDecoder:
    def __init__(self, design_variables):
        self.design_variables = design_variables

    def decode(self, chromosome):
        def decode_variable(variable_chromosome, lower_bound, upper_bound):
            x = 0
            for i in range(len(variable_chromosome)):
                x += variable_chromosome[i] * 2 ** (len(variable_chromosome) - 1 - i)
            decoded =  lower_bound + x * (upper_bound - lower_bound) / (2 ** len(variable_chromosome) - 1)
            return decoded

        decoded = []
        index = 0
        for variable in self.design_variables:
            num_of_bits = variable['bits']
            lower_bound = variable['lower_bound']
            upper_bound = variable['upper_bound']
            variable_chromosome = chromosome[index:index + num_of_bits]
            decoded.append(decode_variable(variable_chromosome, lower_bound, upper_bound))
            index += num_of_bits

        return decoded