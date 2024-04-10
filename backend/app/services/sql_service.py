from contextlib import contextmanager
from contextvars import ContextVar
from sqlalchemy import Engine
from sqlalchemy.orm import Session


class SQLService:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self.session: ContextVar[None | Session] = ContextVar("session", default=None)

    @contextmanager
    def scoped_session(self):
        session = self.session.get()
        if session is not None:
            yield session
            return

        with Session(self.engine, expire_on_commit=False) as session:
            self.session.set(session)
            try:
                yield session
            finally:
                self.session.set(None)
