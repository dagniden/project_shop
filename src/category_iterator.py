class CategoryIterator:

    def __init__(self, category_obj) -> None:
        self.category_obj = category_obj
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index + 1 < len(self.category_obj.products):
            self.__index += 1
            return self.category_obj.products[self.__index]
        else:
            raise StopIteration
