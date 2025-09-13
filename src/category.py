from src.product import Product


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
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[str]:
        result = []
        for item in self.__products:
            result.append(str(item))
        return result
