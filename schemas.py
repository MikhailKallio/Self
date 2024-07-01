from pydantic import BaseModel


class ClientCreate(BaseModel):

    name: str
    email: str


class AccountCreate(BaseModel):

    client_id: int
    balance: float
