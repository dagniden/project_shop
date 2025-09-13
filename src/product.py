from __future__ import annotations


class Product:
    """Класс продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, new_product: dict, product_list: list[Product] | None = None) -> Product:
        if product_list:
            for product in product_list:
                if product.name == new_product.get("name"):
                    product.quantity += 1
                    new_price = new_product.get("price")
                    if new_price is not None:
                        product.price = max(new_price, product.price)

        return Product(**new_product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_value: float) -> None:
        if new_value > 0:
            self.__price = new_value
        elif new_value < self.__price:
            user_input = input("Подтвердите понижение цены товара (y/n): ")
            if user_input.lower() == "y":
                self.__price = new_value
        else:
            print("Цена не должна быть нулевая или отрицательная")
