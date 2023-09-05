class GachaException(ValueError):
    pass


class InvalidPool(GachaException):
    def __init__(self) -> None:
        super().__init__("Pool cannot be used because it is in an invalid state")


class NotEnoughCards(GachaException):
    def __init__(self) -> None:
        super().__init__("Pool does not have enough cards remaining for a pull")
