from utils import getValueOrDefault, chunks
from random import randrange, shuffle, random, choice
from copy import copy
class Individual:
	def __init__(self, vars):
		self.vars = vars

	def generate(self, cities):
		city = cities['Escondidos']
		for _ in range(randrange(3, 10)):
			selectedTravel = city.travels[randrange(len(city.travels))]
			self.vars.append(selectedTravel)
			city = selectedTravel.destiny
	
	def crossover(self, other):
		individuals = [[], []]
		chunkedSelf = chunks(self.vars, 3)
		chunkedOther = chunks(other.vars, 3)

		for i in range(3):
			shuffle(individuals)
			if i != 0:
				individuals[0][-1].destiny = chunkedSelf[i][0].origin
				individuals[1][-1].destiny = chunkedOther[i][0].origin
			individuals[0] += chunkedSelf[i]
			individuals[1] += chunkedOther[i]

		return Individual(individuals[0]), Individual(individuals[1])

	# def crossover(self, other):
	# 	individuals = [[], []]
	# 	chunkedSelf = chunks(self.vars, 2)
	# 	chunkedOther = chunks(other.vars, 2)

	# 	individuals[0] += chunkedSelf[0]
	# 	individuals[1] += chunkedOther[0]

	# 	individuals[1][-1].destiny = chunkedSelf[1][0].origin
	# 	individuals[0][-1].destiny = chunkedOther[1][0].origin

	# 	individuals[1] += chunkedSelf[1]
	# 	individuals[0] += chunkedOther[1]

	# 	return Individual(individuals[0]), Individual(individuals[1])

	# def insert(self):
	# 	choosenIndex = randrange(1, len(self.vars))
	# 	travel = self.vars[choosenIndex]
	# 	try:
	# 		nextTravel = self.vars[choosenIndex + 1]
	# 	except IndexError:
	# 		nextTravel = None
	# 	origin = travel.origin
	# 	possibleTravels = [t for t in origin.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.origin.name]
	# 	# if len(possibleTravels) == 0:
	# 	# 	print(f"travels {origin.name}")
	# 	# 	print()
	# 	# 	for t in origin.travels:
	# 	# 		print(f"De {t.origin.name} para {t.destiny.name}")
	# 	# 	print()
	# 	# 	print(f"index escolhido: {choosenIndex}")
	# 	# 	for t in self.vars:
	# 	# 		print(f"De {t.origin.name} para {t.destiny.name}")
	# 	# 	print()
	# 	newTravel = possibleTravels[randrange(len(possibleTravels))]
	# 	travel.destiny = newTravel.origin
	# 	if nextTravel:
	# 		nextTravel.origin = newTravel.destiny
	# 	self.vars.insert(choosenIndex + 1, newTravel)
	# 	# lastCity = self.vars[-1].destiny
	# 	# travel = choice(lastCity.travels)
	# 	# self.vars.append(travel)
	
	def insert(self):
		choosenIndex = randrange(1, len(self.vars))
		travel = self.vars[choosenIndex]
		try:
			nextTravel = self.vars[choosenIndex + 1]
		except IndexError:
			nextTravel = None
		destiny = travel.destiny
		if nextTravel:
			possibleTravels = [t for t in destiny.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.origin.name and t.destiny.name != nextTravel.destiny.name]
		else:
			possibleTravels = [t for t in destiny.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.origin.name]
		newTravel = copy(possibleTravels[randrange(len(possibleTravels))])
		travel.destiny = newTravel.origin
		if nextTravel:
			nextTravel.origin = newTravel.destiny
		self.vars.insert(choosenIndex + 1, newTravel)

	def insert(self):
		index = randrange(1, len(self.vars))






































	# def flip(self):
	# 	choosenIndex = randrange(1,len(self.vars))
	# 	travel = self.vars[choosenIndex]
	# 	try:
	# 		nextTravel = self.vars[choosenIndex + 1]
	# 	except IndexError:
	# 		nextTravel = None
	# 	origin = travel.origin
	# 	possibleTravels = [t for t in origin.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.origin.name]
	# 	# if len(possibleTravels) == 0: 
	# 	# 	print("origin travels")
	# 	# 	for t in origin.travels:
	# 	# 		print(f"De {t.origin.name} para {t.destiny.name}")
	# 	# 	print()
	# 	# 	print(f"index escolhido: {choosenIndex}")
	# 	# 	for t in self.vars:
	# 	# 		print(f"De {t.origin.name} para {t.destiny.name}")
	# 	newTravel = possibleTravels[randrange(len(possibleTravels))]
	# 	travel.origin = newTravel.origin
	# 	travel.destiny = newTravel.destiny
	# 	if nextTravel:
	# 		nextTravel.origin = newTravel.destiny

	def flip(self):
		choosenIndex = randrange(1,len(self.vars))
		travel = self.vars[choosenIndex]
		try:
			nextTravel = self.vars[choosenIndex + 1]
		except IndexError:
			nextTravel = None
		origin = travel.origin
		if nextTravel:
			possibleTravels = [t for t in origin.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.destiny.name and t.destiny.name != nextTravel.destiny.name]
		else:
			possibleTravels = [t for t in origin.travels if t.destiny.name != travel.destiny.name and t.destiny.name != travel.destiny.name]
		# if len(possibleTravels) != 0:
			# print(f"travels {origin.name}")
			# print()
			# for t in origin.travels:
			# 	print(f"De {t.origin.name} para {t.destiny.name}")
			# print()
			# print(f"index escolhido: {choosenIndex}")
			# for t in self.vars:
			# 	print(f"De {t.origin.name} para {t.destiny.name}")
			# print()
		newTravel = copy(possibleTravels[randrange(len(possibleTravels))])
		travel.destiny = newTravel.destiny
		if nextTravel:
			nextTravel.origin = newTravel.destiny

	def remove(self):
		if len(self.vars) > 3:
			removedIndex = randrange(1, len(self.vars))
			travel = self.vars[removedIndex]

			try:
				nextTravel = self.vars[removedIndex + 1]
			except IndexError:
				nextTravel = None
			
			previousTravel = self.vars[removedIndex - 1]
			if (nextTravel):
				previousTravel.destiny = nextTravel.origin
			self.vars.pop(removedIndex)
			# if len(self.vars) <= 3: return
			# self.vars.pop()

	def mutate(self, n = 1, probability = 0.4):
		for _ in range(n):
			if random() < probability:
				# choosenMutation = choice([self.insert, self.flip, self.remove])
				# choosenMutation = choice([self.insert, self.remove])
				# choosenMutation()
				self.flip()

	def fitness(self):
		score = 0
		totalDuration = 0
		totalWeight = 0
		totalStolen = 0
		totalDebt = 0
		visitedCities = {}
		# Regra forte
		for travel in self.vars:
			timeCost = getValueOrDefault(travel.destiny.item, 'timeCost')
			weight = getValueOrDefault(travel.destiny.item, 'weight')
			stolen = getValueOrDefault(travel.destiny.item, 'price')

			totalDuration += travel.duration + timeCost
			totalWeight += weight
			totalStolen += stolen
			totalDebt += travel.price

			try:
				score -= 200_000
				visitedCities[travel.destiny.name] += 1
			except KeyError:
				visitedCities[travel.destiny.name] = 1

		if (totalDuration > 72):
			score -= 700_000
		
		if (totalWeight > 20):
			score -= 700_000

		if (self.vars[-1].destiny.name != 'Escondidos'):
			score -= 700_000
		
		score += (totalStolen - totalDebt) / (totalDuration + totalWeight)

		return score

	def __str__(self):
		return " | ".join([str(var) for var in self.vars])