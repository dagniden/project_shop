class MixinLog:

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        values = ", ".join(map(str, self.__dict__.values()))
        return f"{self.__class__.__name__}({values})"
