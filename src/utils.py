import json


from src.category import Category
from src.product import Product


def read_json(filename: str) -> list[dict]:
    """Читает json файл и возвращает список словарей"""
    with open(filename, "r", encoding="UTF-8") as json_file:
        return json.load(json_file)


def create_objects_from_json(data_json: list[dict]) -> list[Category]:
    """Возвращает список объектов с типом Category"""
    categories = []
    for category in data_json:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
