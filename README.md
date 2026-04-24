# 📌 API de Cadastro de Usuários

Esta é uma API RESTful desenvolvida para realizar o gerenciamento de usuários, implementando as operações básicas de um CRUD (Create, Read, Update, Delete).

## 🚀 Objetivo

O principal objetivo da API é permitir o cadastro e a manutenção de usuários, armazenando informações essenciais como:

* Nome
* E-mail
* Senha

## 🛠️ Tecnologias Utilizadas

* **Python**
* **SQLAlchemy** para ORM e integração com banco de dados SQL
* **Banco de Dados Relacional (SQL)**
* Validação de dados com **Regex** (especialmente para e-mails)

## 📂 Funcionalidades

A API oferece as seguintes operações:

* **Criar usuário**
  Permite cadastrar um novo usuário com nome, e-mail e senha.

* **Listar usuários**
  Retorna todos os usuários cadastrados.

* **Buscar usuário por ID**
  Recupera os dados de um usuário específico.

* **Atualizar usuário**
  Permite editar informações de um usuário existente.

* **Deletar usuário**
  Remove um usuário do sistema.

## ✅ Validações

* O campo **e-mail** é validado utilizando uma expressão regular (Regex), garantindo que o formato informado seja válido.
* Campos obrigatórios:

  * Nome
  * E-mail
  * Senha

## 🗄️ Banco de Dados

A API utiliza um banco de dados relacional (SQL), com mapeamento objeto-relacional feito através do **SQLAlchemy**, facilitando a manipulação e persistência dos dados.

## 📌 Estrutura Básica do Usuário

```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "********"
}
```

## ⚠️ Observações

* Recomenda-se o uso de hash para armazenamento de senhas em ambientes de produção.
* A API pode ser facilmente integrada com sistemas frontend ou outros serviços.

---

Feito para fins de estudo e prática de desenvolvimento de APIs 🚀
