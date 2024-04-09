import random
from src.lib.quantum_genetic_algorithm import QuantumIndividual
from src.lib.classical_genetic_algorithm import ClassicalGeneticAlgorithm
from src.lib.classical_genetic_algorithm.generation import Generation as ClassicalGeneticAlgorithmModel
from src.lib.genetic_algorithm import GeneticAlgorithm

def f(x):
    x1, x2, x3 = x
    return x1 ** 2 + x2 ** 2 + x3 ** 2


design_variables = [
    {'name': 'x', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12},
    {'name': 'y', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12},
    {'name': 'z', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12}
]

seed = 42
random.seed(seed)


def run_classical_genetic_algorithm():
    evolution_strategy = {
        'num_of_generations': 300,
        'population_size': 120,
        'elitism_rate': 0.2,
        'crossover_elitism_rate': 0.5,
        'mutation_rate': 0.05
    }

    cga = GeneticAlgorithm(
        design_variables=design_variables,
        fitness_function=f,
        evolution_strategy=evolution_strategy,
        model=ClassicalGeneticAlgorithmModel
    )

    cga.solve()

    optimal_individual = cga.get_optimal_individual()
    print(f'Optimal Individual: {optimal_individual.decode()}')
    print(f'Optimal Fitness: {optimal_individual.fitness_score}')

    cga.plot_convergence()


def run_quantum_genetic_algorithm():
    evolution_strategy = {
        'num_of_generations': 300,
        'population_size': 120,
        'elitism_rate': 0.2,
        'crossover_elitism_rate': 0.5,
        'mutation_rate': 0.05
    }

    # qca = QuantumGeneticAlgorithm(
    #     design_variables=design_variables,
    #     fitness_function=f,
    #     evolution_strategy=evolution_strategy
    # )

    # qca.solve()

    # quantum_individual = QuantumIndividual(design_variables, f)
    # measurement = quantum_individual.measure()
    # print(f'Measurement: {measurement["measurement"]}')
    # print(f'Decoded Measurement: {measurement["decoded_measurement"]}')
    # print(f'Fitness Score: {measurement["fitness_score"]}')


if __name__ == '__main__':
    run_classical_genetic_algorithm()
    # run_quantum_genetic_algorithm()
