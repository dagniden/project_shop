from unittest.mock import patch

from pytest import CaptureFixture

from src.category import Category
from src.main import main


def test_main_output(capsys: CaptureFixture[str]) -> None:
    # Сбрасываем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Запускаем main()
    with patch("builtins.input", return_value="y"):
        main()

    # Перехватываем stdout
    output = capsys.readouterr().out

    # # Проверяем, что первые print показывают список продуктов
    # assert "Samsung Galaxy S23 Ultra 1" in output
    # assert "Iphone 15" in output
    # assert "Xiaomi Redmi Note 11" in output
    # assert "Смартфоны" in output
    # assert "Samsung Galaxy S23 Ultra 2" in output
    #
    # assert Category.category_count == 1
    # assert Category.product_count == 4
