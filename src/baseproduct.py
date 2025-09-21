from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Класс для представления продукта."""

    @abstractmethod
    def __init__(self, name: str, description: str, quantity: int):
        """Инициализирует продукт с именем, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.quantity = quantity
