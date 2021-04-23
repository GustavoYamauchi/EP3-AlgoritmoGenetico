import pandas as pd
from utils import *
from geneticAlgorithm import GeneticAlgorithm
from population import Population

cities = createCities()
linkTravels(cities)
initialPopulation = Population([])
initialPopulation.generate(10, cities)

geneticAlgorithm = GeneticAlgorithm(initialPopulation, 10000)
individual, generation, fitness = geneticAlgorithm.letsBora()

print(f"indivíduo: {individual}, geração: {generation}, fitness: {fitness}")

# print(f"population {len(initialPopulation.individuals)}")
# for ind in initialPopulation.individuals:
# 	print(f"ind {len(ind.vars)}")
# 	[print(f"\t{travel.origin.name, travel.destiny.name}") for travel in ind.vars]

# for city in cities.values():
# 	print('------------------------------------------------------------------------')
# 	print(f"City -> {city.name}")
# 	print(f"Item -> {city.item}")
# 	print(f"Travels {len(city.travels)}")
# 	[print(f"\t{travel}") for travel in city.travels]
# 	print('------------------------------------------------------------------------')
