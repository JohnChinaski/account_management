from typing import List, Optional
from pydantic import BaseModel
import datetime


# ---------- ACCOUNTS ----------
class Account(BaseModel):
    saldo: float
    limiteSaqueDiario: float
    tipoConta: int

    class Config:
        orm_mode = True


class AccountConsult(Account):
    idConta: int
    dataCriacao: datetime.date


# ---------- TRANSACTIONS ----------
class Transactions(BaseModel):
    idTransacao: int
    idConta: int
    valor: float
    dataTransacao: datetime.date

    class Config:
        orm_mode = True


class TransactionsCreate(Transactions):
    pass


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
