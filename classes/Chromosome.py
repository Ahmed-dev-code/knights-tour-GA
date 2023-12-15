from __future__ import annotations
import random

class Chromosome:
    
    def __init__(self, genes=None):    
        if genes is None:
            self.genes = [random.randint(1, 8) for _ in range(63)]
        else:
            self.genes = genes
    
    def crossover(self, partner: 'Chromosome') -> 'Chromosome':
        # Single-point crossover
        crossover_point = random.randint(1, len(self.genes) - 1)
        new_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        return Chromosome(new_genes)
    
    def mutation(self, mutation_rate: float):
        # Introduce random mutations with a given probability (mutation_rate)
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                # Replace a gene with a random move
                self.genes[i] = random.randint(1, 8)
                
        


