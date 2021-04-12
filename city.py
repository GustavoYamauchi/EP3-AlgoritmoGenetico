class City:
    def __init__(self, name, item):
        self.name = name
        self.item = item
        self.travels = []

    def addTravel(self, travel):
        self.travels.append(travel)

    def __str__(self):
        return f"{self.name} - {self.item} - {self.travels}"
