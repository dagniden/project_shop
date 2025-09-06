import os

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_phone() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_tv() -> Product:
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category(product_phone: Product, product_tv: Product) -> Category:
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_phone, product_tv],
    )


@pytest.fixture
def data_dir() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    return data_dir
