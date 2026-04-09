from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/users")
def create_user(usuario: User):
    if not email_validator(usuario):
        return {'error': 'E-mail invalido'}
    if not name_validator(usuario):
        return {'error': 'Nome invalido'}
    if not password_validator(usuario):
        return {'error': 'Senha invalida'}
    return {'message': 'Usuario criado com sucesso'}



def email_validator(usuario: User):
    email_usuario = usuario.email.strip()
    if email_usuario.count('@') != 1:
        return False
    posicao_arroba = email_usuario.index('@')
    if posicao_arroba == 0:
        return False
    verifica_arroba = email_usuario[posicao_arroba + 1:]
    if verifica_arroba == '':
        return False
    if verifica_arroba.count('.') == 0:
        return False
    else:
        return True


def name_validator(usuario: User):
    if usuario.name == '':
        return False
    else:
        return True


def password_validator(usuario: User):  
    senha = usuario.password
    tamanho_senha = len(senha)
    if tamanho_senha < 6:
        return False
    elif senha.isdigit():
        return False       
    elif not any(char.isalpha() for char in senha):
        return False
    else:
        return True
            
