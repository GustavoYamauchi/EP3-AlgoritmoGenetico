from population import Population

class GeneticAlgorithm:
	def __init__(self, initialPopulation, generations):
		self.population = initialPopulation
		self.generations = generations

	def letsBora(self):
		bestGlobal = (None, 0, float('-inf'))

		for generation in range(self.generations):
			self.population.sort()

			bestLocal = self.population.individuals[0].fitness()
			if (bestLocal > bestGlobal[2]):
				bestGlobal = (self.population.individuals[0], generation, bestLocal)

			individuals = self.population.individuals[0:3]

			for j in range(int(len(self.population.individuals) / 2) - 1):
				individualA, individualB = self.population.select()
				# print(f"pré crossover A: ")
				# print(individualA)
				# print()
				# print(f"pré crossover B: ")
				# print(individualB)
				aNewIndividual, otherNewIndividual = individualA.crossover(individualB)
				# print()
				# print(f"pós crossover A: ")
				# print(aNewIndividual)
				# print()
				# print(f"pós crossover B: ")
				# print(otherNewIndividual)
				# print()

				aNewIndividual.mutate()
				otherNewIndividual.mutate()

				individuals += [aNewIndividual, otherNewIndividual]

			self.population = Population(individuals)

		return bestGlobal
