from db import  db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(200))
    documento = db.Column(db.Numeric)
    contatos = db.Column(db.BLOB)

    def __init__(self,nome,documento):
        self.nome = nome
        self.documento = documento