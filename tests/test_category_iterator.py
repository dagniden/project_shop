import pytest

from src.category import Category
from src.category_iterator import CategoryIterator


def test_category_iterator(category: Category) -> None:
    category_iterator = CategoryIterator(category)
    assert next(category_iterator) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 1 шт."
    assert next(category_iterator) == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'

    with pytest.raises(StopIteration):
        next(category_iterator)
