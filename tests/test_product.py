from src.category import Category
from src.product import Product


def test_product(product_phone: Product) -> None:
    assert isinstance(product_phone, Product)
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5


def test_category(category: Category) -> None:
    assert isinstance(category, Category)
    assert category.name == "Телевизоры"
    assert (
        category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    for product in category.products:
        assert isinstance(product, Product)
    assert category.category_count == 1
    assert category.product_count == 2
