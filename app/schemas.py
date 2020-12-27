from typing import List, Optional
from pydantic import BaseModel
import datetime


# ---------- ACCOUNTS ----------
class Accoun(BaseModel):
    idConta: int
    idPessoa: int
    saldo: float
    limiteSaqueDiario: float
    flagAtivo: bool
    tipoConta: int
    dataCriacao: datetime.date

    class Config:
        orm_mode = True


class AccounCreate(Accoun):
    pass


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
