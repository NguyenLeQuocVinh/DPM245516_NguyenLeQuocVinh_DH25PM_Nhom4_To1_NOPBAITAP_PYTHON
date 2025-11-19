class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id};{self.name}"


class Product:
    def __init__(self, id, name, price, category_id):
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id

    def __str__(self):
        return f"{self.id};{self.name};{self.price};{self.category_id}"
