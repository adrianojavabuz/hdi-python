# Teste HDI
## API Usuário e Contatos

Esta API retorna um CRUD de usuários e contatos esta desenvolvida utilizando python como linguagem de desenvolvimento.


## Tecnologias utilizadas

- Flask==1.0.2 - HTML enhanced for web apps!
- Flask-SQLAlchemy==2.3.1 
- flask-marshmallow=0.9.0 

## Instalação

Flask run [To run](https://flask.palletsprojects.com/en/2.0.x/quickstart/#what-to-do-if-the-server-does-not-start).

Instalar as dependencias e startar o servidor.

```sh
cd api-flask
flask run
```

## Banco de Dados

Quando a API é iniciada ela cria o banco development.sqlite3 na pasta Raiz da aplicação.
Na pasta raiz temos o arquivo create-table.txt, nesse arquivo temos o script para a criação
das tabelas que a API utiliza : contato, usuario.

Abra o banco development.sqlite3 em algum SGBD ou linha de comando e execute os scripts do arquivo:
create-table.txt.

## POSTMAN

A API sobe na porta 9000, com a uri api.
Endpoints CRUD : 
http://localhost:9000/api/contato
http://localhost:9000/api/usuario