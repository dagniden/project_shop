from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class Category:
    """Класс с категориями продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if issubclass(type(product), (Product, Smartphone, LawnGrass)):
            if product.quantity <= 0:
                raise ZeroProductError("Нельзя добавлять товар с нулевым количеством")
            else:
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> list[str]:
        result = []
        for item in self.__products:
            result.append(str(item))
        return result

    def middle_price(self):
        total_price = sum([p.price for p in self.__products])
        try:
            return round(total_price / self.product_count, 2)
        except ZeroDivisionError:
            return 0


class ZeroProductError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Нельзя добавлять товар с нулевым количеством"

    def __str__(self):
        return self.message
