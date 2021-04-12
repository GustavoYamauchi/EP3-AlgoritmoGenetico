import pandas as pd
from utils import *
from geneticAlgorithm import GeneticAlgorithm

cities = createCities()
linkTravels(cities)

initialPopulation = createPopulation(cities)
geneticAlgorithm = GeneticAlgorithm(initialPopulation)
geneticAlgorithm.letsBora()

# print(f"population {len(population)}")
# for ind in population:
# 	print(f"ind {len(ind)}")
# 	[print(f"\t{travel.origin.name, travel.destiny.name}") for travel in ind]

# for city in cities.values():
# 	print('------------------------------------------------------------------------')
# 	print(f"City -> {city.name}")
# 	print(f"Item -> {city.item}")
# 	print(f"Travels {len(city.travels)}")
# 	[print(f"\t{travel}") for travel in city.travels]
# 	print('------------------------------------------------------------------------')

# cidades = createCities()
# travles = createTravles(cidades)