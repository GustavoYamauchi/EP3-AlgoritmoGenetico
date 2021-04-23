from utils import *
import copy

cities = createCities()
linkTravels(cities)



vars = [
	Travel(cities['Escondidos'], cities['Lagos']),
	Travel(cities['Lagos'], cities['Porto']),
	Travel(cities['Porto'], cities['Limões']),
	Travel(cities['Limões'], cities['Escondidos']),
]



def insert():
	index = randrange(1, len(vars))
	baseTravel = vars[index - 1]
	nextTravel = vars[index + 1] if index + 1 < len(vars) else None
	newTravel = copy(baseTravel)
	newTravel.origin = baseTravel.destiny
	
	