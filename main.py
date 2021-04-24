from utils import *
from random import seed
from geneticAlgorithm import GeneticAlgorithm
from population import Population

seed()

initialPopulation = Population([])
initialPopulation.generate(10)

geneticAlgorithm = GeneticAlgorithm(initialPopulation, 70000)
individual, generation, fitness, tempoTotal, pesoTotal = geneticAlgorithm.letsBora()

print(f"indivíduo: {individual}, geração: {generation}, fitness: {fitness}, tempo total: {tempoTotal}, pesoTotal: {pesoTotal}")