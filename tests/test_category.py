from src.category import Category
from src.product import Product


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
