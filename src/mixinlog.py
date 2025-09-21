class MixinLog:

    def __init__(self):
        print(self.__repr__())

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.name}, "
                f"{self.description}, "
                f"{self.price}, "
                f"{self.quantity})")
