class MissingElement(ValueError):
    def __init__(self, _type: type, id: str) -> None:
        super().__init__(f"{_type} Could not find record with id: {id}")
        self.id = id
        self.type = _type


class InvalidElement(ValueError):
    def __init__(self, _type: type, reasons: list[str]) -> None:
        super().__init__(f'{_type} was invalid: {",".join(reasons)}')
        self.type = _type
        self.reasons = reasons
