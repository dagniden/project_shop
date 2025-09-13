from __future__ import annotations

from src.category import Category


class CategoryIterator:

    def __init__(self, category_obj: Category) -> None:
        self.category_obj = category_obj
        self.__index = -1

    def __iter__(self) -> CategoryIterator:
        return self

    def __next__(self) -> str:
        if self.__index + 1 < len(self.category_obj.products):
            self.__index += 1
            return self.category_obj.products[self.__index]
        else:
            raise StopIteration
