from individual import Individual
from random import sample

class Population:
	def __init__(self, individuals):
		self.individuals = individuals
		
	def generate(self, size, cities):
		for _ in range(size):
			ind = Individual([])
			ind.generate(cities)

			self.individuals.insert(len(self.individuals), ind)

	def sort(self):
		self.individuals = sorted(self.individuals, key=lambda individual: individual.fitness(), reverse=True)
	
	def select(self):
		selectedIndividuals = sample(self.individuals, k=2)
		return selectedIndividuals
