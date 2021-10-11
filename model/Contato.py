from db import db

class Contato(db.Model):
    __tablename__ = 'contato'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200))
    telefone = db.Column(db.Numeric)
    flag = db.Column(db.Integer)

    def __init__(self, email, telefone, flag):
        self.email = email
        self.telefone = telefone
        self.flag = flag

    def __repr__(self):
        return '<Contato: email -> %s telefone -> %s>' % (self.email, self.telefone)