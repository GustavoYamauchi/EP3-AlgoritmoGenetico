import pandas as pd
from city import City
from item import Item
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

def createTravels():
	createdTravels = {}
	for _, row in cidades.iterrows():
		createdTravels[f"{row['origin']}-{row['destiny']}"] = (row['duration'], row['price'])
	return createdTravels

def getValueOrDefault(obj, item, default = 0):
		return getattr(obj, item) if obj else default

def chunks(arr, numOfChunks):
	# l % n sub-arrays of size l//n + 1 and the rest of size l//n
	n1 = len(arr)%numOfChunks
	s2 = int(len(arr)/numOfChunks)
	s1 = s2+1
	n2 = int((len(arr)/s2-n1*s1 if n1 == 0 else (len(arr)-n1*s1)/s2))
	arrayFinal = []
	[arrayFinal.append(arr[i*s1:i*s1+s1]) for i in range(n1)]
	[arrayFinal.append(arr[i*s2+n1*s1:i*s2+s2+n1*s1]) for i in range(n2)]

	return arrayFinal