import random
from src.lib.evolutionary_algorithms import CEASolver, QEASolver, QEAModel


seed = 42
random.seed(seed)


def f(x):
    x1, x2, x3 = x
    return x1 ** 2 + x2 ** 2 + x3 ** 2


design_variables = [
    {'name': 'x', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12},
    {'name': 'y', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12},
    {'name': 'z', 'lower_bound': -200, 'upper_bound': 200, 'bits': 12}
]

ea_model_params = [
    {
        'name': 'Classical Evolutionary Algorithm',
        'strategy': {
            'num_of_generations': 300,
            'population_size': 120,
            'elitism_rate': 0.2,
            'crossover_elitism_rate': 0.5,
            'mutation_rate': 0.05
        },
        'solver': CEASolver
    }, 
    {
        'name': 'Quantum Evolutionary Algorithm',
        'strategy': {
            'num_of_generations': 1000,
            'population_size': 30,
        },
        'solver': QEAModel
    }
]


def run_ea_models():
    for params in ea_model_params:
        print(f'Running {params["name"]}...')

        solver = params['solver']
        strategy = params['strategy']

        ea_solver = solver(
            evolution_strategy=strategy,
            design_variables=design_variables,
            fitness_function=f,
        )

        ea_solver.solve()

        # optimal_individual = ea_solver.get_optimal_individual()
        # print(f'Optimal Individual: {optimal_individual.decode()}')
        # print(f'Optimal Fitness: {optimal_individual.fitness_score}')

        # ea_solver.plot_convergence()


if __name__ == '__main__':
    run_ea_models()
