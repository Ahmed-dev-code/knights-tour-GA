import random
from classes.Chromosome import Chromosome
import config

moves = [
    (-2, 1),  # 1: up-right
    (-1, 2),  # 2: right_up
    (1, 2),  # 3: right_down
    (2, 1),  # 4: down_right
    (2, -1),  # 5: down_left
    (1, -2),  # 6: left_down
    (-1, -2),  # 7: left_up
    (-2, -1),  # 8: up_left
]


class Knight:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = Chromosome()
        else:
            self.chromosome = chromosome
        self.position = config.STARTING_POSITION
        self.fitness = 0
        self.path = []
        self.path.append(self.position)

    def move_forward(self, direction):
        new_x = self.position[0] + moves[direction - 1][0]
        new_y = self.position[1] + moves[direction - 1][1]
        self.position = (new_x, new_y)

    def trace_back(self, direction):
        initial_x = self.position[0] - moves[direction - 1][0]
        initial_y = self.position[1] - moves[direction - 1][1]

        self.position = (initial_x, initial_y)

    def is_inside(self, position):
        return 0 <= position[0] <= 7 and 0 <= position[1] <= 7

    def is_legal(self, position: "tuple", path: "list") -> bool:
        """
        check if the position (x,y) is inside the chessboard
        and the position is not already in the path (not visited)
        """
        return self.is_inside(position) and (position not in path)

    def check_moves(self):
        # check the validity of each move in the chromosome,
        # a move is valid when : applying the move_forward places the knight in new position that is inside the board
        # and the new position is not already visited
        # a not valid move should be corrected if is possible
        i = 0
        cycle_direction = random.choice([-1, 1])
        for gene in self.chromosome.genes:
            self.move_forward(gene)
            if self.is_legal(self.position, self.path):
                self.path.append(self.position)

            else:
                self.trace_back(gene)
                gene_corrected = False
                for _ in range(7):
                    gene = (gene + cycle_direction - 1) % 8 + 1
                    self.move_forward(gene)
                    if self.is_legal(self.position, self.path):
                        self.chromosome.genes[i] = gene
                        self.path.append(self.position)
                        gene_corrected = True
                        break
                    else:
                        self.trace_back(gene)
                if not gene_corrected:
                    self.chromosome.genes[i] = gene
                    self.move_forward(gene)
                    self.path.append(self.position)

            i += 1

    def evaluate_fitness(self):
        visited_pos = []
        for position in self.path:
            if self.is_inside(position) and position not in visited_pos:
                self.fitness += 1
                visited_pos.append(position)
            else:
                break
