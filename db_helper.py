from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_config import settings_db


class BDHelper:
    def __init__(self, url: str):
        self.engine = create_engine(url=url, echo=True)

        self.session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=False, autocommit=False, autoflush=False
        )


db = BDHelper(url=settings_db.database_url)
