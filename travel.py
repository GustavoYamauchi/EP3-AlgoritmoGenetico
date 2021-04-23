class Travel:
    def __init__(self, origin, destiny, duration, price):
        self.origin = origin
        self.destiny = destiny
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"{self.origin.name} -> {self.destiny.name}"