from src.smartphone import Smartphone


def test_product_smartphone(product_smartphone: Smartphone) -> None:
    assert issubclass(type(product_smartphone), Smartphone)
    assert product_smartphone.name == "Iphone 15"
    assert product_smartphone.description == "512GB, Gray space"
    assert product_smartphone.price == 210000.0
    assert product_smartphone.quantity == 8
    assert product_smartphone.efficiency == 98.2
    assert product_smartphone.model == "15"
    assert product_smartphone.memory == 512
    assert product_smartphone.color == "Gray space"
