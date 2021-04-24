from utils import *

class Data:
	__instance = None
	cities = createCities()
	travels = createTravels()

	@staticmethod 
	def getInstance():
		if Data.__instance == None:
			Data()
		return Data.__instance

	def __init__(self):
		if Data.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			Data.__instance = self

	def getValuesForCities(self, name1, name2):
		try:
			return self.travels[f"{name1}-{name2}"]
		except KeyError:
			return self.travels[f"{name2}-{name1}"]
