from src.product import Product


class Category:
    """Класс с категориями продуктов"""
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products
        self.category_count += 1
        self.product_count += len(products)
