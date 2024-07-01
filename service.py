from sqlalchemy import select

from db_helper import db
from models import Client, Account


def add_new_client(
        name: str,
        email: str,
):
    with db.session_factory() as session:
        new_client = Client(
            name=name,
            email=email
        )
        session.add(new_client)
        session.commit()


def add_new_account(
        client_id: int,
        balance: float
):
    with db.session_factory() as session:
        new_account = Account(
            client_id=client_id,
            balance=balance
        )
        session.add(new_account)
        session.commit()


def get_accounts_by_client_id(client_id: int):
    with db.session_factory() as session:
        stmt = select(Account).where(Account.client_id == client_id)
        result = session.execute(stmt)
        accounts = result.scalars().all()
        return accounts
