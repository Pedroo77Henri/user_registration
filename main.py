from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import re
from database import SessionLocal, engine, Base
from models import UserAccount
from sqlalchemy.orm import Session


app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/users")
def create_user(usuario: User, db: Session = Depends(get_db)):
    resultado = validator_user(usuario)
    if resultado:
        raise HTTPException(status_code=422, detail=resultado)
    db_user = UserAccount(
        name=usuario.name,
        email=usuario.email,
        password=usuario.password)
    try: 
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {'Mensagem': 'Usuario criado com sucesso'}
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Não foi possível criar usuario por dado invalido")


def email_validator(email):
    return bool(re.match(r"[a-zA-Z0-9._-]+@[a-z]+([.][a-z]+)+", email))


def name_validator(usuario: User):
    if usuario.name == '':
        return False
    return True


def password_validator(usuario: User):  
    senha = usuario.password
    tamanho_senha = len(senha)
    if tamanho_senha < 6:
        return False
    if senha.isdigit():
        return False       
    if not any(char.isalpha() for char in senha):
        return False
    return True
       
    
def validator_user(usuario: User):
    erros = []
    if not email_validator(usuario.email):
        erros.append('E-mail invalido')
    if not name_validator(usuario):
        erros.append('Nome invalido')
    if not password_validator(usuario):
        erros.append('Senha invalida')
    return erros