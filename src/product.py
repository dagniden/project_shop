from __future__ import annotations

from src.baseproduct import BaseProduct
from src.mixinlog import MixinLog


class Product(BaseProduct, MixinLog):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует продукт с именем, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity

        super().__init__()

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Складывает общую стоимость двух продуктов."""
        if issubclass(type(other), type(self)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Складывать можно только объекты класса Product")

    @property
    def price(self) -> float:
        """Возвращает текущую цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_value: float) -> None:
        """Устанавливает новую цену продукта с проверкой."""
        if new_value < 0:
            print("Цена не должна быть нулевая или отрицательная")

        if new_value < self.__price:
            user_input = input("Подтвердите понижение цены товара (y/n): ")
            if user_input.lower() == "y":
                self.__price = new_value
        else:
            self.__price = new_value

    @classmethod
    def new_product(cls, new_product: dict, product_list: list | None = None) -> Product:
        """Создаёт новый продукт или обновляет количество и цену существующего."""
        if product_list:
            for product in product_list:
                if product.name == new_product.get("name"):
                    product.quantity += 1
                    new_price = new_product.get("price")
                    if new_price is not None:
                        product.price = max(new_price, product.price)

        return Product(**new_product)
