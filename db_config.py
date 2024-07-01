from typing import Optional
from os import getenv

from pydantic import PostgresDsn
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class ConfigDataBaseAccounts(BaseSettings):
    DB_USER: str = getenv("DB_USER")
    DB_PASS: str = getenv("DB_PASS")
    DB_NAME: str = getenv("DB_NAME")
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: str = getenv("DB_PORT")

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (f'postgresql://{self.DB_USER}:{self.DB_PASS}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')


settings_db = ConfigDataBaseAccounts()
