from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/users")
def create_user(usuario: User):
    resultado = validator_user(usuario)
    if not resultado:
        return {'Mensagem': 'Criado com sucesso'}
    raise HTTPException(status_code=422, detail=resultado)



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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
