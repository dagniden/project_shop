import os

from src.utils import create_objects_from_json, read_json
from src.category import Category


def test_read_json(data_dir: str) -> None:
    filename = os.path.join(data_dir, "products.json")
    raw_data = read_json(filename)

    assert isinstance(raw_data, list)


def test_create_objects_from_json(data_dir: str) -> None:
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    filename = os.path.join(data_dir, "products.json")
    raw_data = read_json(filename)
    objects = create_objects_from_json(raw_data)
    assert isinstance(objects, list)
    assert objects[0].name == "Смартфоны"
    assert objects[1].name == "Телевизоры"

    # Подсчет количества продуктов
    assert objects[0].product_count == 4
    assert objects[1].product_count == 4

    # Подсчет количества категорий
    assert objects[1].category_count == 2
