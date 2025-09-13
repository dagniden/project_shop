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
