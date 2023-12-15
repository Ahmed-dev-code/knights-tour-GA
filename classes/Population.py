from typing import List, Tuple
from classes.Knight import Knight
import random


class Population:
    def __init__(self, population_size: int):
        self.population_size = population_size
        self.knights = self.generate_initial_population()
        self.generation = 1

    def generate_initial_population(self) -> List[Knight]:
        # Generate a list of knights for the initial population
        return [Knight() for _ in range(self.population_size)]

    def check_population(self):
        # Check if the population is valid
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self) -> Tuple[Knight, int]:
        # Evaluate the fitness of each knights
        for knight in self.knights:
            knight.evaluate_fitness()

        # Sort the knights based on their fitness values
        self.knights = sorted(
            self.knights, key=lambda knight: knight.fitness, reverse=True
        )

        # return the best knight and its fitness value
        return self.knights[0], self.knights[0].fitness

    def tournament_selection(self, size: int = 3) -> List[Knight]:
        # Check if the population size is sufficient for the tournament
        if len(self.knights) < size:
            raise ValueError("Population size is less than the tournament size.")

        # Randomly sample n knights from the population
        selected_knights = random.sample(self.knights, size)

        # Return the best two knights with the highest fitness
        return sorted(
            selected_knights, key=lambda knight: knight.fitness, reverse=True
        )[:2]

    def create_new_generation(self):
        mutation_rate = 1 / 63

        # create a new generation of knights by applying crossover and mutation
        new_generation = []
        for _ in range(self.population_size // 2):
            # select parents
            parent1, parent2 = self.tournament_selection()
            # crossover
            child_chromosome = parent1.chromosome.crossover(parent2.chromosome)
            child2_chromosome = parent2.chromosome.crossover(parent1.chromosome)
            # mutation
            child_chromosome.mutation(mutation_rate)
            child2_chromosome.mutation(mutation_rate)

            # create new knights with the new chromosomes
            new_knight = Knight(chromosome=child_chromosome)
            new_knight2 = Knight(chromosome=child2_chromosome)

            new_generation.append(new_knight)
            new_generation.append(new_knight2)

        # replace the old generation with the new one
        self.knights = new_generation
        self.generation += 1
