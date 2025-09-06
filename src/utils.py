import json


from src.category import Category
from src.product import Product


def read_json(filename: str) -> list[dict]:
    with open(filename, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def create_objects_from_json(data: list[dict]) -> list[Category]:
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
