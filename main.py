from classes.Population import Population
from classes.Board import Board
import config


def main():
    population_size = config.POPULATION_SIZE
    # create the initial population
    population = Population(population_size)

    while True:
        # check the validity of the current population
        population.check_population()

        # Evaluate the current generation and get the best knight with its fitness value
        best_knight, best_fitness = population.evaluate()
        print(
            "Generation: {} | Fitness: {}".format(population.generation, best_fitness)
        )
        if best_fitness == 64:
            # We found the solution
            break

        # Create a new generation
        population.create_new_generation()

    print("Solution found in generation {}!".format(population.generation))
    print("Fitness: {}".format(best_fitness))
    print("Path: {}".format(best_knight.path))

    board = Board()
    board.main(best_knight.path)


if __name__ == "__main__":
    main()
