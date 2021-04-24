from utils import getValueOrDefault, chunks
from data import Data
from random import randrange, shuffle, random, choice

class Individual:
	def __init__(self, vars):
		self.vars = vars

	def generate(self):
		cities = Data.getInstance().cities

		self.vars = ['Escondidos']
		for _ in range(randrange(3, 10)):
			citiesCopy = list(cities.keys()).copy()
			citiesCopy.remove('Escondidos')
			selectedCity = choice(citiesCopy)
			self.vars.append(selectedCity)
	
	def crossover(self, other):
		individuals = [[], []]
		nChunks = 3
		chunkedSelf = chunks(self.vars, nChunks)
		chunkedOther = chunks(other.vars, nChunks)

		for i in range(nChunks):
			shuffle(individuals)

			individuals[0] += chunkedSelf[i]
			individuals[1] += chunkedOther[i]

		return Individual(individuals[0]), Individual(individuals[1])
	
	def insertVar(self, baseIndividuals):
		mutatingIndividuals = []
		mutatingIndividuals = baseIndividuals.copy()
		choosenIndex = randrange(1, len(mutatingIndividuals))
		possibleCities = [key for key in list(Data.getInstance().cities.copy().keys()) if key not in self.vars or key == 'Escondidos']
		newCity = choice(possibleCities)

		mutatingIndividuals.insert(choosenIndex, newCity)
		return mutatingIndividuals

	def flip(self, mutatingIndividuals):
		choosenIndex = randrange(1, len(mutatingIndividuals))	
		possibleCities = [key for key in list(Data.getInstance().cities.copy().keys()) if key not in self.vars or key == 'Escondidos']
        
		newCity = choice(possibleCities)

		mutatingIndividuals[choosenIndex] = newCity

		return mutatingIndividuals

	def remove(self, mutatingIndividuals):
		if len(mutatingIndividuals) <= 3: return mutatingIndividuals
		choosenIndex = randrange(1, len(mutatingIndividuals))
		if choosenIndex + 1 < len(mutatingIndividuals):
			if mutatingIndividuals[choosenIndex - 1] == mutatingIndividuals[choosenIndex + 1]:
				choosenMutation = choice([self.insertVar, self.flip])
				return choosenMutation(mutatingIndividuals)
		mutatingIndividuals.pop(choosenIndex)
		return mutatingIndividuals

	def mutate(self, n = 3, probability = 1):
		for _ in range(n):
			if random() < probability:
				choosenMutation = choice([self.insertVar, self.flip, self.remove])
				return Individual(choosenMutation(self.vars))
		return self

	def fitness(self):
		score = 0
		totalDuration = 0
		totalWeight = 0
		totalStolen = 0
		totalDebt = 0
		visitedCities = {}

		data = Data.getInstance()
		cities = data.cities

		for i in range(len(self.vars) - 1):
			currentCity = cities[self.vars[i]]
			nextCity = cities[self.vars[i+1]]

			if (self.vars[i] == self.vars[i+1]):
				return -9_000_000, 0, 0
				
			try:
				if visitedCities[currentCity.name] and currentCity.name != 'Escondidos':
					score -= 200_000
			except KeyError:
				visitedCities[currentCity.name] = True
			
			timeCost = getValueOrDefault(currentCity.item, 'timeCost')
			weight = getValueOrDefault(currentCity.item, 'weight')
			stolen = getValueOrDefault(currentCity.item, 'price')

			travelData = data.getValuesForCities(currentCity.name, nextCity.name)

			totalDuration += travelData[0] + timeCost
			totalWeight += weight
			totalStolen += stolen
			totalDebt += travelData[1]

		if (totalDuration > 72):
			score -= 700_000
		
		if (totalWeight > 20):
			score -= 700_000

		if (self.vars[-1] != 'Escondidos'):
			score -= 700_000
		
		score += totalStolen - totalDebt

		return score, totalDuration, totalWeight

	def __str__(self):
		return " -> ".join([str(var) for var in self.vars])