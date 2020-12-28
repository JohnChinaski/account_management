from typing import List
from fastapi import FastAPI, Depends, HTTPException
from app import models, crud, schemas
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- ACCOUNTS ----------
@app.post("/account/", response_model=schemas.AccountConsult, tags=["Account"])
def create_account(item: schemas.AccountCreate, db: Session = Depends(get_db)):
    check_person = crud.get_person_by_id(db=db, idPessoa=item.idPessoa)
    if check_person:
        return crud.create_account(db=db, item=item)
    else:
        raise HTTPException(status_code=404, detail=f"Usuario ID {item.idPessoa} nao cadastrado.")


@app.get("/account/transactions/{idConta}", response_model=List[schemas.TransactionsConsult], tags=["Account"])
def get_all_transactions_by_idconta(idConta: int, db: Session = Depends(get_db)):
    db_account = crud.get_all_transactions_by_idconta(db=db, idConta=idConta)
    if not db_account:
        raise HTTPException(status_code=404, detail=f"idConta {idConta} nao possui transacoes cadastradas.")
    else:
        return db_account


@app.put("/account/block/{idConta}", response_model=schemas.AccountUpdate, tags=["Account"])
def block_account(idConta: int, db: Session = Depends(get_db)):
    try:
        block = crud.block_account(db=db, idConta=idConta)
        return "OK!"
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro as tentar bloquear idConta {idConta}. Error: {e}")


@app.put("/account/unlock/{idConta}", response_model=schemas.AccountUpdate, tags=["Account"])
def unlock_account(idConta: int, db: Session = Depends(get_db)):
    try:
        block = crud.unlock_account(db=db, idConta=idConta)
        return "OK!"
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro as tentar bloquear idConta {idConta}. Error: {e}")


@app.get("/account/saldo/{idConta}", response_model=schemas.Account, tags=["Account"])
def get_account_saldo(idConta: int, db: Session = Depends(get_db)):
    account_balance = crud.get_account_saldo(db=db, idConta=idConta)
    return account_balance


@app.get("/account/idPessoa/{idPessoa}", response_model=List[schemas.AccountConsult], tags=["Account"])
def get_account_by_idpessoa(idPessoa: int, db: Session = Depends(get_db)):
    check_person = crud.get_person_by_id(db=db, idPessoa=idPessoa)
    if not check_person:
        raise HTTPException(status_code=404, detail=f"Usuario ID {idPessoa} nao cadastrado.")
    else:
        db_account = crud.get_account_by_idpessoa(db, idPessoa=idPessoa)
        if not db_account:
            raise HTTPException(status_code=404, detail=f"Usuario ID {idPessoa} nao possui conta(s) cadastradas.")
        else:
            return db_account


@app.get("/account/idConta/{idConta}", response_model=schemas.AccountConsult, tags=["Account"])
def get_account_by_idconta(idConta: int, db: Session = Depends(get_db)):
    db_account = crud.get_account_by_idconta(db, idConta=idConta)
    if not db_account:
        raise HTTPException(status_code=404, detail=f"Nao encontrado nenhuma conta para Person ID {idConta}.")
    else:
        return db_account


@app.get("/allaccounts/", response_model=List[schemas.AccountConsult], tags=["Account"])
def get_all_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accounts = crud.get_all_accounts(db=db, skip=skip, limit=limit)
    if accounts:
        return accounts
    else:
        raise HTTPException(status_code=400, detail="Nenhuma Person cadastrada.")


# ---------- PERSONS ----------
@app.post("/person/", response_model=schemas.GetAllPersons, tags=["Person"])
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    check_person = crud.get_person_by_cpf(db=db, cpf=person.cpf)
    if check_person:
        raise HTTPException(status_code=400, detail="Documento ja cadastrado.")
    else:
        return crud.create_person(db=db, person=person)


@app.get("/person/cpf/{cpf}", response_model=schemas.GetAllPersons, tags=["Person"])
def get_person_by_cpf(cpf: str, db: Session = Depends(get_db)):
    db_user = crud.get_person_by_cpf(db, cpf=cpf)
    if not db_user:
        raise HTTPException(status_code=404, detail=f"Usuario CPF {cpf} nao cadastrado.")
    else:
        return db_user


@app.get("/person/id/{idPessoa}", response_model=schemas.GetAllPersons, tags=["Person"])
def get_person_by_id(idPessoa: int, db: Session = Depends(get_db)):
    db_user = crud.get_person_by_id(db, idPessoa=idPessoa)
    if not db_user:
        raise HTTPException(status_code=404, detail=f"Usuario ID {idPessoa} nao cadastrado.")
    else:
        return db_user


@app.get("/allpersons/", response_model=List[schemas.GetAllPersons], tags=["Person"])
def get_all_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persons = crud.get_all_persons(db, skip=skip, limit=limit)
    if persons:
        return persons
    else:
        raise HTTPException(status_code=400, detail="Nenhuma Person cadastrada.")


# ---------- TRANSACTIONS ----------
@app.post("/account/debit/", response_model=schemas.TransactionsConsult, tags=["Transaction"])
def account_debit(item: schemas.TransactionsCreate, db: Session = Depends(get_db)):
    check_account = crud.get_account_by_idconta(db, idConta=item.idConta)
    if check_account:
        transaction = crud.account_debit(db=db, item=item)
        return transaction
    else:
        raise HTTPException(status_code=404, detail=f"Nenhuma conta encontrada para idConta {item.idConta}.")


@app.post("/account/credit/", response_model=schemas.TransactionsConsult, tags=["Transaction"])
def account_credit(item: schemas.TransactionsCreate, db: Session = Depends(get_db)):
    check_account = crud.get_account_by_idconta(db, idConta=item.idConta)
    if check_account:
        transaction = crud.account_credit(db=db, item=item)
        return transaction
    else:
        raise HTTPException(status_code=404, detail=f"Nenhuma conta encontrada para idConta {item.idConta}.")


@app.get("/transactions/dataIni/{dataini}/dataFim/{datafim}/idConta/{idConta}/",
         response_model=List[schemas.TransactionsConsult],
         tags=["Transaction"])
def get_all_transctions_by_date_and_idconta(idConta: int, dataini: str, datafim: str, db: Session = Depends(get_db)):
    start_date = datetime.datetime.strptime(dataini, "%d-%m-%Y")
    end_date = datetime.datetime.strptime(datafim, "%d-%m-%Y")
    transactions = crud.get_account_transaction_by_date_idconta(db=db,
                                                                dataini=start_date,
                                                                datafim=end_date,
                                                                idConta=idConta)
    if transactions:
        return transactions
    else:
        raise HTTPException(status_code=400,
                            detail=f"Nenhuma transaction para idConta {idConta} entre as datas {dataini} e {datafim}")


@app.get("/transactions/idConta/{idConta}/",
         response_model=List[schemas.TransactionsConsult],
         tags=["Transaction"])
def get_all_transctions_by_idconta(idConta: int, db: Session = Depends(get_db)):
    transactions = crud.get_account_transaction_by_idconta(db=db, idConta=idConta)
    if transactions:
        return transactions
    else:
        raise HTTPException(status_code=400, detail=f"Nenhuma transaction para idConta {idConta}")


@app.get("/transactions/dataIni/{dataini}/dataFim/{datafim}/",
         response_model=List[schemas.TransactionsConsult],
         tags=["Transaction"])
def get_all_transctions_by_date(dataini: str, datafim: str, db: Session = Depends(get_db)):
    start_date = datetime.datetime.strptime(dataini, "%d-%m-%Y")
    end_date = datetime.datetime.strptime(datafim, "%d-%m-%Y")
    transactions = crud.get_account_transaction_by_date(db=db,
                                                        dataini=start_date,
                                                        datafim=end_date)
    if transactions:
        return transactions
    else:
        raise HTTPException(status_code=400,
                            detail=f"Nenhuma transaction entre as datas {dataini} e {datafim}")


@app.get("/alltransactions/", response_model=List[schemas.TransactionsConsult], tags=["Transaction"])
def get_all_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_transactions = crud.get_all_transactions(db=db,
                                                skip=skip,
                                                limit=limit)
    if not db_transactions:
        raise HTTPException(status_code=404, detail=f"Nenhuma transação cadastrada cadastradas.")
    else:
        return db_transactions
