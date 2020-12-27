from typing import List, Optional
from pydantic import BaseModel
import datetime


# ---------- ACCOUNTS ----------
class Account(BaseModel):
    saldo: float

    class Config:
        orm_mode = True


class AccountBasic(Account):
    limiteSaqueDiario: float
    tipoConta: int


class AccountCreate(AccountBasic):
    idPessoa: int


class AccountConsult(AccountBasic):
    idConta: int
    idPessoa: int
    dataCriacao: datetime.date
    flagAtivo: bool


class AccountUpdate(BaseModel):
    pass

    class Config:
        orm_mode = True


# ---------- TRANSACTIONS ----------
class Transactions(BaseModel):
    idConta: int

    class Config:
        orm_mode = True


class TransactionsCreate(Transactions):
    valor: float


class TransactionsConsult(Transactions):
    idTransacao: int
    descricao: str
    valor: float
    dataTransacao: datetime.date


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
