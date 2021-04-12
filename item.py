class Item:
    def __init__(self, name, weight, timeCost, price):
        self.name = name
        self.weight = weight
        self.timeCost = timeCost
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.weight} - {self.timeCost} - {self.price}"