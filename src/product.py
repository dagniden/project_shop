class Product:
    """Класс продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        return Product(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_value):
        if new_value > 0:
            self.__price = new_value
        else:
            print("Цена не должна быть нулевая или отрицательная")