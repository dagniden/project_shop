from src.lawngrass import LawnGrass


def test_product_smartphone(product_lawngrass: LawnGrass) -> None:
    assert issubclass(type(product_lawngrass), LawnGrass)
    assert product_lawngrass.name == "Газонная трава"
    assert product_lawngrass.description == "Элитная трава для газона"
    assert product_lawngrass.price == 500.0
    assert product_lawngrass.quantity == 20
    assert product_lawngrass.country == "Россия"
    assert product_lawngrass.germination_period == "7 дней"
    assert product_lawngrass.color == "Зеленый"
