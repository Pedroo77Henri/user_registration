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
    result = validator_user(usuario)
    if result:
        raise HTTPException(status_code=422, detail=result)
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
        raise HTTPException(status_code=500, detail="Não foi possível criar usuario")

class UserUpdate(BaseModel):
    name: str
    email: str

    @app.put("/users/{user_id}")
    def edit_user(user_id: int, new_user: UserUpdate, db: Session = Depends (get_db)):
            edit_id = db.query(UserAccount).filter(UserAccount.id == user_id).first()
            if edit_id is None:
                raise HTTPException(status_code=404, detail="Id não encontrado")
            if not name_validator(new_user.name):
                raise HTTPException(status_code=422, detail="Não foi possível atualizar o nome, invalido")
            if not email_validator(new_user.email):
                raise HTTPException(status_code=422, detail="Não foi possível atualizar o email, invalido")
            edit_id.name = new_user.name
            edit_id.email = new_user.email
            try:
                db.commit()
                db.refresh(edit_id)
                return{'Mensagem': 'Usuario atualizado'}
            except Exception:
                db.rollback()
                raise HTTPException(status_code=500, detail="Erro na edição")
        

        
        



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