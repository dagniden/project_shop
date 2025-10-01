# Учебный проект

Категории и продукты

## Структура проекта

- `category.py` — класс `Category` для работы с категориями товаров.
- `product.py` — класс `Product` для описания отдельных товаров.
- `utils.py` — вспомогательные функции:
    - `read_json` — чтение данных из JSON-файла.
    - `create_objects_from_json` — создание объектов `Category` и `Product` на основе данных из JSON.

## Классы
- Добавлен базовый класс для всех продуктов `BaseProduct`
- Добавлены классы-наследники для класса `Product`:
  - `Smartphone` — с дополнительными свойствами: `efficiency`, `model`, `memory`, `color`.
  - `LawnGrass` — с дополнительными свойствами: `country`, `germination_period`, `color`.
- Операция сложения товаров теперь возможна только для объектов одного типа.  
  При попытке сложить разные типы выбрасывается `TypeError`.
- Метод добавления продуктов в категорию защищён от добавления объектов, не являющихся наследниками `Product`.
- Добавлены тесты для новой функциональности, старые тесты остаются актуальными.
- Добавлен класс миксин `MixinLog`, который при создании объекта продукта выводит информацию о нем  

## Пример данных JSON

```json
[
    {
        "name": "Смартфоны",
        "description": "Мобильные устройства",
        "products": [
            {
                "name": "Samsung Galaxy S23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "iPhone 15 Pro",
                "description": "512GB, Белый цвет",
                "price": 210000.0,
                "quantity": 3
            }
        ]
    }
]
```

## Пример использования

```python
from src.utils import read_json, create_objects_from_json

data = read_json("data.json")
categories = create_objects_from_json(data)

for category in categories:
    print(f"Категория: {category.name}")
    for product in category.products:
        print(f"- {product.name}: {product.price} руб. (осталось {product.quantity} шт.)")
```

## Требования

* Python 3.10+



