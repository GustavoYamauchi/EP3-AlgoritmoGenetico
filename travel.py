class Travel:
    def __init__(self, origin, destiny, price, duration):
        self.origin = origin
        self.destiny = destiny
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"{self.origin} - {self.destiny} - {self.price} - {self.duration}"