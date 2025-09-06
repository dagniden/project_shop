import os

from src.utils import create_objects_from_json, read_json


def test_read_json(data_dir: str) -> None:
    filename = os.path.join(data_dir, "products.json")
    raw_data = read_json(filename)

    assert isinstance(raw_data, list)


def test_create_objects_from_json(data_dir: str) -> None:
    filename = os.path.join(data_dir, "products.json")
    raw_data = read_json(filename)
    objects = create_objects_from_json(raw_data)
    assert isinstance(objects, list)
    assert objects[0].name == "Смартфоны"
    assert objects[1].name == "Телевизоры"

    assert objects[0].product_count == 3
    assert objects[1].product_count == 1

    assert objects[1].category_count == 1
