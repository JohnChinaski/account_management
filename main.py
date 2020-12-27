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


# ---------- PERSONS ----------
@app.post("/person/", response_model=schemas.PersonCreate)
def create_user(person: schemas.Persons, db: Session = Depends(get_db)):
    check_person = crud.get_person_by_cpf(db=db, cpf=person.cpf)
    if check_person:
        raise HTTPException(status_code=400, detail="Documento ja cadastrado.")
    else:
        return crud.create_person(db=db, person=person)


@app.get("/allpersons/", response_model=List[schemas.GetAllPersons])
def get_all_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persons = crud.get_all_persons(db, skip=skip, limit=limit)
    if persons:
        return persons
    else:
        raise HTTPException(status_code=400, detail="Nenhuma Person cadastrada.")
