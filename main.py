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
@app.post("/account/", response_model=schemas.Account)
def create_account(account: schemas.Account, db: Session = Depends(get_db)):
    return crud.create_account(db=db, item=account)


@app.get("/account/idPessoa/{idPessoa}", response_model=List[schemas.AccountConsult])
def get_account_by_idpessoa(idPessoa: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_account = crud.get_account_by_idpessoa(db, idPessoa=idPessoa)
    if not db_account:
        raise HTTPException(status_code=404, detail=f"Usuario ID {idPessoa} nao possui conta(s) cadastradas.")
    else:
        return db_account


@app.get("/account/idConta/{idConta}", response_model=schemas.AccountConsult)
def get_account_by_idconta(idConta: int, db: Session = Depends(get_db)):
    db_account = crud.get_account_by_idconta(db, idConta=idConta)
    if not db_account:
        raise HTTPException(status_code=404, detail=f"Nao encontrado nenhuma conta para Person ID {idConta}.")
    else:
        return db_account


# ---------- PERSONS ----------
@app.post("/person/", response_model=schemas.PersonCreate)
def create_user(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    check_person = crud.get_person_by_cpf(db=db, cpf=person.cpf)
    if check_person:
        raise HTTPException(status_code=400, detail="Documento ja cadastrado.")
    else:
        return crud.create_person(db=db, person=person)


@app.get("/person/cpf/{cpf}", response_model=schemas.GetAllPersons)
def get_user_by_cpf(cpf: str, db: Session = Depends(get_db)):
    db_user = crud.get_person_by_cpf(db, cpf=cpf)
    if not db_user:
        raise HTTPException(status_code=404, detail=f"Usuario CPF {cpf} nao cadastrado.")
    else:
        return db_user


@app.get("/person/id/{idPessoa}", response_model=schemas.GetAllPersons)
def get_user_by_id(idPessoa: int, db: Session = Depends(get_db)):
    db_user = crud.get_person_by_id(db, idPessoa=idPessoa)
    if not db_user:
        raise HTTPException(status_code=404, detail=f"Usuario ID {idPessoa} nao cadastrado.")
    else:
        return db_user


@app.get("/allpersons/", response_model=List[schemas.GetAllPersons])
def get_all_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persons = crud.get_all_persons(db, skip=skip, limit=limit)
    if persons:
        return persons
    else:
        raise HTTPException(status_code=400, detail="Nenhuma Person cadastrada.")
