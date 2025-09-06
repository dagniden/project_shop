from pytest import CaptureFixture

from src.category import Category
from src.main import main


def test_main_output(capsys: CaptureFixture[str]) -> None:
    # Сбросим счётчики перед тестом, чтобы не было влияния от других тестов
    Category.category_count = 0
    Category.product_count = 0

    main()  # запускаем основную функцию

    # Захватываем stdout
    captured = capsys.readouterr()

    output = captured.out.splitlines()

    # Проверяем первые выводы (поля первого продукта)
    assert "Samsung Galaxy S23 Ultra" in output
    assert "256GB, Серый цвет, 200MP камера" in output
    assert "180000.0" in output
    assert "5" in output

    # Проверяем создание категорий
    assert "Телевизоры" in output

    # # Проверяем что счётчики классов корректные
    assert str(Category.category_count) in output
    assert str(Category.product_count) in output
