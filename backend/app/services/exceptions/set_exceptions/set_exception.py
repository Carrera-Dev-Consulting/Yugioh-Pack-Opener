class SetException(ValueError):
    def __init__(self, set_id: str, message: str = "Set was invalid") -> None:
        super().__init__(f"set_id: {set_id}, {message}")
        self.set_id = set_id
