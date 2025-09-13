from unittest.mock import patch

from src.product import Product


def test_product(product_phone: Product) -> None:
    assert isinstance(product_phone, Product)
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 1


def test_new_product(product_phone: Product) -> None:
    products = [product_phone]
    assert product_phone.quantity == 1
    product2 = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 1,
    }

    Product.new_product(product2, products)
    assert product_phone.quantity == 2
    assert product_phone.price == 200000.0


def test_price_setter(product_phone: Product) -> None:
    product_phone.price = 150000
    with patch("builtins.input", return_value="y"):
        assert product_phone.price == 150000


def test_product_str(product_phone: Product) -> None:
    assert str(product_phone) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 1 шт."


def test_product_add(product_phone: Product) -> None:
    assert (product_phone + product_phone) == 360000.0
