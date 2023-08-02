from sqlalchemy.orm import Session


class Repository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type or exc_value or exc_tb:
            # exception thrown so rolling back what we did
            self.session.rollback()
            return False
        else:
            self.session.commit()
