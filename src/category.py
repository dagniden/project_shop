from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products_list: list[Product]):
        self.name = name
        self.description = description
        self.products = products_list
        self.category_count += 1
        self.product_count += len(products_list)
