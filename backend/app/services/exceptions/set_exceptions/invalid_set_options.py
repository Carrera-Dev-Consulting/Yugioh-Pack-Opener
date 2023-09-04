from .set_exception import SetException


class InvalidSetOptions(SetException):
    def __init__(self, set_id: str) -> None:
        super().__init__(set_id, "Set options could not be understood")
