from typing import List, Optional
from pydantic import BaseModel
import datetime


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


class Transactions(BaseModel):
    idTransacao: int
    idConta: int
    valor: float
    dataTransacao: datetime.date

    class Config:
        orm_mode = True


class TransacCreate(Transactions):
    pass


class Persons(BaseModel):
    idPessoa: int
    nome: str
    cpf: str
    dataNascimento: datetime.date

    class Config:
        orm_mode = True


class PersonsCreate(Persons):
    pass