from decimal import Decimal


class Product:
    def __init__(self, category: str, name: str, price: Decimal):
        self.category = category
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.category}\t{self.name}\t{self.price}"
