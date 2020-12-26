from sqlalchemy.orm import Session
from . import schemas, models


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
    return data


def get_account_transaction_by_date():
    """
      Função retorna todas as transações em um determinado range de datas de uma determinada account.
  """
    pass

# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
