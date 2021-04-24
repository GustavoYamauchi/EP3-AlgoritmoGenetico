class City:
    def __init__(self, name, item):
        self.name = name
        self.item = item

    def __str__(self):
        return f"{self.name} - {self.item}"
