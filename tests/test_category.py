from src.category import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert isinstance(category, Category)
    assert category.name == "Телевизоры"

    assert category.category_count == 1
    assert category.product_count == 2


def test_add_product(product_phone: Product, category: Category) -> None:
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    category.add_product(product_phone)
    category.product_count = 1
    category.category_count = 1


def test_category_str(category: Category) -> None:
    assert str(category) == "Телевизоры, количество продуктов: 8 шт."


def test_category_middle_price(product_phone: Product) -> None:
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "Категория смартфонов", [product_phone, product_phone, product_phone])
    assert category1.middle_price() == 180000.0

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
