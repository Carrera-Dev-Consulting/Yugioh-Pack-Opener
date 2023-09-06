import os.path
import json
from typing import Protocol

from fastapi.encoders import jsonable_encoder

from app.models import User, Result
from .exceptions.users import UserNotFound, InvalidUser


class UserRepository(Protocol):
    def get_user_by_id(self, user_id: str) -> User:
        pass

    def add_user(self, user: User) -> User:
        pass


authentication_keys = {"public_key", "sign_count", "credential_id", "challenge"}


class FileUserRepository:
    def __init__(self, filename) -> None:
        self.db: dict[str, User | dict] = {}
        self.filename = filename

        if not os.path.exists():
            self._store_changes()
        else:
            with open(filename, "r") as fp:
                self.db = json.load(fp)

    def _store_changes(self):
        with open(self.filename) as fp:
            json.dump(jsonable_encoder(self.db), fp)

    def get_user_by_id(self, user_id: str) -> User:
        if user_id not in self.db:
            raise UserNotFound(user_id)

        return User.model_validate(self.db[user_id])

    def is_valid_user(self, user: User) -> Result[bool]:
        missing_keys = [key for key in authentication_keys if key not in user.meta]
        if missing_keys:
            return Result(
                value=False,
                errors=[f"{key} is missing from meta" for key in missing_keys],
            )
        return Result(value=True)

    def add_user(self, user: User) -> User:
        result = self.is_valid_user(user)
        if result.errors:
            raise InvalidUser(result.errors)

        self.db[user.username] = user
        self._store_changes()

        return User.model_validate(user)
