import pytest

from src.category import Category, ZeroProductError
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


def test_category_zero_product_error(category: Category) -> None:
    product1 = Product("Товар без количества", "Тестовый товар", 500, 1)
    product1.quantity = 0

    with pytest.raises(ZeroProductError, match="Нельзя добавлять товар с нулевым количеством"):
        category.add_product(product1)
