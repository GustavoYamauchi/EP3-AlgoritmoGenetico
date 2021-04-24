from individual import Individual
from random import sample
from data import Data

class Population:
	def __init__(self, individuals):
		self.individuals = individuals
		
	def generate(self, size):
		for _ in range(size):
			individual = Individual([])
			individual.generate()

			self.individuals.append(individual)

	def sort(self):
		self.individuals = sorted(self.individuals, key=lambda individual: individual.fitness()[0], reverse=True)
	
	def select(self):
		return sample(self.individuals, k=2)
