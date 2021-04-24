from population import Population

class GeneticAlgorithm:
	def __init__(self, initialPopulation, generations):
		self.population = initialPopulation
		self.generations = generations

	def letsBora(self):
		bestGlobal = (None, 0, float('-inf'), 0, 0)

		for generation in range(self.generations):
			if generation % 2500 == 0: print(f"Geração atual: {generation}")
			self.population.sort()

			bestLocal = self.population.individuals[0].fitness()
			if (bestLocal[0] > bestGlobal[2]):
				bestGlobal = (self.population.individuals[0], generation, bestLocal[0], bestLocal[1], bestLocal[2])

			individuals = self.population.individuals[0:2]

			for j in range(int(len(self.population.individuals) / 2) - 1):
				individualA, individualB = self.population.select()

				individualA = individualA.mutate()
				individualB = individualB.mutate()

				aNewIndividual, otherNewIndividual = individualA.crossover(individualB)
				individuals += [aNewIndividual, otherNewIndividual]

			self.population = Population(individuals)

		return bestGlobal
