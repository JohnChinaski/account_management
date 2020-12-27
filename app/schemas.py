from typing import List, Optional
from pydantic import BaseModel
import datetime


# ---------- ACCOUNTS ----------
class Account(BaseModel):
    saldo: float

    class Config:
        orm_mode = True


class AccountBasic(BaseModel):
    limiteSaqueDiario: float
    tipoConta: int


class AccountConsult(AccountBasic):
    idConta: int
    dataCriacao: datetime.date
    flagAtivo: bool


# ---------- TRANSACTIONS ----------
class Transactions(BaseModel):
    idConta: int

    class Config:
        orm_mode = True


class TransactionsCreate(Transactions):
    valor: float


# ---------- PERSONS ----------
class Persons(BaseModel):
    nome: str
    cpf: str

    class Config:
        orm_mode = True


class PersonCreate(Persons):
    dataNascimento: str


class GetAllPersons(Persons):
    idPessoa: int
    dataNascimento: datetime.date
