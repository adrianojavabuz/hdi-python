#from flask import Blueprint, jsonify
#from flask_sqlalchemy import model
#from config import ma
#from model.Contato import Contato

#contato = Blueprint('contato', __name__)
'''
class ContatoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
       model = Contato

contatos_schema = ContatoSchema(many=True)

@contato.route('/', methods=['GET'])
def main():
    return 'teste'

@contato.route('/contato', methods = ['GET'])
def findAllContato():
    contatos = Contato.query.all()
    res = contatos_schema.dump(contatos)
  #  json_users = []

 
    return jsonify(res);
    '''