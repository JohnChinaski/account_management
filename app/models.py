from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
import datetime

from app.database import Base


class Persons(Base):
    __tablename__ = "persons"

    idPessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    dataNascimento = Column(Date)

    account = relationship("Accounts", back_populates="persons")


class Accounts(Base):
    __tablename__ = "accounts"

    idConta = Column(Integer, primary_key=True, index=True)
    idPessoa = Column(ForeignKey("Persons.idPessoa"))
    saldo = Column(Float)
    limiteSaqueDiario = Column(Float)
    flagAtivo = Column(Boolean, default=True)
    tipoConta = Column(Integer)
    dataCriacao = Column(Date, default=datetime.date.today())

    person = relationship("Persons", back_populates="accounts")


class Transactions(Base):
    __tablename__ = "transactions"

    idTransacao = Column(Integer, primary_key=True, index=True)
    idConta = Column(ForeignKey("Account.idConta"))
    valor = Column(Float)
    dataTransacao = Column(Date, default=datetime.date.today())

    account = relationship("Accounts", back_populates="transactions")
