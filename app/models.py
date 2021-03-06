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

    account = relationship("Accounts", back_populates="person")


class Accounts(Base):
    __tablename__ = "accounts"

    idConta = Column(Integer, primary_key=True, index=True)
    idPessoa = Column(Integer, ForeignKey("persons.idPessoa"))
    saldo = Column(Float, default=0.0)
    limiteSaqueDiario = Column(Float, default=0.0)
    flagAtivo = Column(Boolean, default=True)
    tipoConta = Column(Integer)
    dataCriacao = Column(Date, default=datetime.date.today())

    person = relationship("Persons", back_populates="account")
    transaction = relationship("Transactions", back_populates="account")


class Transactions(Base):
    __tablename__ = "transactions"

    idTransacao = Column(Integer, primary_key=True, index=True)
    idConta = Column(Integer, ForeignKey("accounts.idConta"))
    valor = Column(Float)
    descricao = Column(String)
    dataTransacao = Column(Date, default=datetime.date.today())

    account = relationship("Accounts", back_populates="transaction")
