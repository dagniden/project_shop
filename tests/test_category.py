from src.category import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert isinstance(category, Category)
    assert category.name == "Телевизоры"

    assert category.category_count == 1
    assert category.product_count == 2

def test_add_product(product_phone, category: Category):
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    category.add_product(product_phone)
    category.product_count = 1
    category.category_count = 1