from src.product import Product


def test_product(product_phone: Product) -> None:
    assert isinstance(product_phone, Product)
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5
