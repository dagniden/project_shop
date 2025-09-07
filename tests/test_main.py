import re
from src.main import main
from src.category import Category


def test_main_output(capsys):
    # Сбрасываем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Запускаем main()
    main()

    # Перехватываем stdout
    output = capsys.readouterr().out

    # Проверяем, что первые print показывают список продуктов
    assert "Samsung Galaxy S23 Ultra 1" in output
    assert "Iphone 15" in output
    assert "Xiaomi Redmi Note 11" in output
    assert "Смартфоны" in output
    assert "Samsung Galaxy S23 Ultra 2" in output