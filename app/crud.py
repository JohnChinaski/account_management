from sqlalchemy.orm import Session
from . import schemas, models
import datetime


# ACCOUNT
def get_account_saldo_by_id(db: Session, idConta: int):
    """
        Função que retorna o saldo se uma determinada Account.
    """
    account = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    if account:
        return account.saldo
    else:
        return False


def create_account(db: Session, user: schemas.AccounCreate, content):
    """
        Função para criação de uma Account.
    """
    db_account = models.Accounts(idPessoa=content.get("idPessoa"),
                                 saldo=content.get("saldo"),
                                 limiteSaqueDiario=content.get("limiteSaqueDiario"),
                                 flagAtivo=content.get("flagAtivo"),
                                 tipoConta=content.get("tipoConta"),
                                 )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def update_saldo_add_value():
    """
        Função para adição de saldo em uma derterminada Account.
    """
    pass


def update_saldo_remove_value():
    """
        Função para remoção de saldo em uma derterminada Account.
    """
    pass


def block_account():
    """
        Função para bloqueio uma derterminada Account.
    """
    pass


def get_account_transaction(db: Session, idConta: int):
    transactions = db.query(models.Transactions).filter(models.Transactions.idConta == idConta)

    transactions_list = []

    for t in transactions:
        data = {
            "idTransacao": t.idTransacao,
            "idConta": t.idConta,
            "valor": t.valor,
            "dataTransacao": t.dataTransacao,
        }

        transactions_list.append(data)
    return transactions_list


def get_account_transaction_by_date():
    """
      Função retorna todas as transações em um determinado range de datas de uma determinada account.
    """
    pass


# PERSONS
def get_person_by_cpf(db: Session, cpf: str):
    check_person = db.query(models.Persons).filter(models.Persons.cpf == cpf).first()
    if check_person:
        return check_person
    else:
        return False


def get_person_by_id(db: Session, idPessoa: int):
    check_person = db.query(models.Persons).filter(models.Persons.idPessoa == idPessoa).first()
    if check_person:
        return check_person
    else:
        return False


def get_all_persons(db: Session, skip: int = 0, limit: int = 100):
    """
        Função que retorna todas as Persons cadastradas
    """
    persons = db.query(models.Persons).offset(skip).limit(limit).all()
    return persons


def create_person(db: Session, person: schemas.Persons):
    """
        Função para criação de um Person.
    """
    db_person = models.Persons(
        nome=person.nome,
        cpf=person.cpf,
        dataNascimento=person.dataNascimento,
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
