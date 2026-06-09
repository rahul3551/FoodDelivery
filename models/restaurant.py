
class Restaurant:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Restaurant: {self.name}, City: {self.city}"