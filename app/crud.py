from sqlalchemy.orm import Session
from . import schemas, models
import datetime


# ---------- ACCOUNT ----------
def get_account_saldo(db: Session, idConta: int):
    """
        Função que retorna o saldo se uma determinada Account.
    """
    account = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    if account:
        return {"saldo": account.saldo}
    else:
        return False


def create_account(db: Session, item: schemas.AccountCreate):
    """
        Função para criação de uma Account.
    """
    db_account = models.Accounts(**item.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_account_by_idpessoa(db: Session, idPessoa: int):
    """
        Função retorna uma Account específica para uma determinada Person.
    """
    check_account = db.query(models.Persons).filter(models.Persons.idPessoa == idPessoa).first()
    accounts = check_account.account
    if accounts:
        return accounts
    else:
        return False


def get_account_by_idconta(db: Session, idConta: int):
    """
        Função retorna uma Account buscando pelo ID.
    """
    accounts = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    if accounts:
        return accounts
    else:
        return False


def account_debit(db: Session, item: schemas.TransactionsCreate):
    """
        Função para criação de uma Transaction (DEBITO) e atualizar o salda da Account referente.
    """
    db_transaction = models.Transactions(**item.dict())
    db_transaction.descricao = "DEBITO"
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    # update
    old_balance = db_transaction.account.saldo
    db_transaction.account.saldo = old_balance - item.valor
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def account_credit(db: Session, item: schemas.TransactionsCreate):
    """
        Função para criação de uma Transaction (CREDITO) e atualizar o salda da Account referente.
    """
    db_transaction = models.Transactions(**item.dict())
    db_transaction.descricao = "CREDITO"
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    # update
    old_balance = db_transaction.account.saldo
    db_transaction.account.saldo = old_balance + item.valor
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def block_account(db: Session, idConta: int):
    """
        Função para bloqueio uma determinada Account.
    """
    account = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    account.flagAtivo = False
    db.commit()
    db.refresh(account)

    return account


def unlock_account(db: Session, idConta: int):
    """
        Função para bloqueio uma determinada Account.
    """
    account = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    account.flagAtivo = True
    db.commit()
    db.refresh(account)

    return account


def get_all_transactions(db: Session, skip: int = 0, limit: int = 100):
    """
        Função que retorna todas as Transactions cadastradas.
    """
    transactions = db.query(models.Transactions).offset(skip).limit(limit).all()

    if transactions:
        return transactions
    else:
        return False


def get_all_transactions_by_idconta(db: Session, idConta: int):
    """
        Função que retorna todas as Transactions cadastradas para uma específica conta.
    """
    check_transactions = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()
    transactions = check_transactions.transaction

    if transactions:
        return transactions
    else:
        return False


def get_all_accounts(db: Session, skip: int = 0, limit: int = 100):
    """
        Função que retorna todas as Accounts cadastradas
    """
    accounts = db.query(models.Accounts).offset(skip).limit(limit).all()
    return accounts


# ---------- TRANSACTIONS ----------
def get_account_transaction_by_date(db: Session, dataini: datetime.date, datafim: datetime.date):
    """
      Função retorna todas as transações em um determinado range de datas.
    """
    check_account = db.query(models.Transactions).filter(
        models.Transactions.dataTransacao.between(dataini, datafim)).all()

    return check_account


def get_account_transaction_by_date_idconta(db: Session, dataini: datetime.date, datafim: datetime.date, idConta: int):
    """
      Função retorna todas as transações em um determinado range de datas de uma determinada account.
    """
    check_account = db.query(models.Transactions).filter(
        models.Transactions.idConta == idConta,
        models.Transactions.dataTransacao.between(dataini, datafim)).all()

    return check_account


# ---------- PERSONS ----------
def get_person_by_cpf(db: Session, cpf: str):
    """
        Função que busca um Person a partir do CPF.
    """
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


def create_person(db: Session, person: schemas.PersonCreate):
    """
        Função para criação de um Person.
    """
    birth_date = datetime.datetime.strptime(person.dataNascimento, "%d-%m-%Y")
    db_person = models.Persons(
        nome=person.nome,
        cpf=person.cpf,
        dataNascimento=birth_date,
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_transactions_by_date_idconta(db: Session, idConta: int, dataini: "str", datafim: "str"):
    check_account = db.query(models.Accounts).filter(models.Accounts.idConta == idConta).first()

    transactions = check_account.transaction
    date_start = datetime.datetime.strptime(dataini, "%d-%m-%Y")
    date_end = datetime.datetime.strptime(datafim, "%d-%m-%Y")
    transaction_by_date = transactions.filter()
