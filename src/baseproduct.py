from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Класс для представления продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, new_product: dict, product_list: list | None = None) -> Any:
        pass
