from fastapi import APIRouter, HTTPException

from db_helper import db
from models import Client, Account
from schemas import ClientCreate, AccountCreate
from service import get_accounts_by_client_id

router = APIRouter(
    prefix="", tags=["Clients"]
)


@router.post("/clients")
def create_new_client(create_client: ClientCreate):
    with db.session_factory() as session:
        new_client = Client(
            name=create_client.name,
            email=create_client.email
        )
        session.add(new_client)
        session.commit()
    return {"message": "The new client has been successfully created!"}


@router.post("/accounts")
def create_new_account(create_account: AccountCreate):
    with db.session_factory() as session:
        existing_client = session.query(Client).filter(
            Client.id == create_account.client_id).first()
        if existing_client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        new_account = Account(
            client_id=create_account.client_id,
            balance=create_account.balance
        )
        session.add(new_account)
        session.commit()
    return {"message": "Your account has been successfully created!"}


@router.get("/clients/{client_id}")
def get_accounts_client(client_id: int):
    with db.session_factory() as session:
        existing_client = session.query(Client).filter(
            Client.id == client_id).first()
        if existing_client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        all_accounts = get_accounts_by_client_id(client_id)
        return all_accounts
