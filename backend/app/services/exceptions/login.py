class InvalidLogin(ValueError):
    def __init__(self) -> None:
        super().__init__("Unable to validate credentials")
