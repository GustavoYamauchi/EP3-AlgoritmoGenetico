import pandas as pd
from city import City
from item import Item
from travel import Travel
from random import randrange

cidades = pd.read_csv("Docs/cidades.csv")

def createCities():
    cities = {}
    citiesUnion = cidades[['origin', 'destiny']].values.ravel('K')
	
    for city in pd.unique(citiesUnion):
        item = createItem(city)
        cities[city] = City(city, item)
    
    return cities

def createItem(city):
    items = pd.read_csv("Docs/itens.csv")
    result = items[items.city == city].values

    if len(result) == 0:
        return None

    name, weight, timeCost, price, city = result[0]
    return Item(name, weight, timeCost, price)

def linkTravels(cities):
	for city in cities.values():
		travels = cidades[cidades.origin == city.name].values
		for cityA, cityB, distance, price in travels:
			# print(cityA, cityB)
			cities[cityA].addTravel(Travel(cities[cityA], cities[cityB], distance, price))
			cities[cityB].addTravel(Travel(cities[cityB], cities[cityA], distance, price))

def createPopulation(cities):
	population = []
	for _0 in range(10):
		travels = []
		city = cities['Escondidos']
		for _1 in range(randrange(3, 10)):
			selectedTravel = city.travels[randrange(13)]
			travels.append(selectedTravel)
			city = selectedTravel.destiny
		
		population.append(travels)
	
	return population

