from . import contato
from flask import request, jsonify
from db import ma, db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from model.Contato import Contato

class ContatoSchema(SQLAlchemyAutoSchema):
    class Meta:
       model = Contato

contatos_schema = ContatoSchema(many=True)

@contato.route('/', methods = ['GET'])
def findAllContato():
    contato = Contato.query.all()
    res = contatos_schema.dump(contato)
 
    return jsonify(res);

@contato.route('/<int:id>', methods = ['GET'])
def findByIdContato(id):
    contato = Contato.query.get(id);

    if(contato is None):
        return "Not Found", 404

    obj = {
            'id': contato.id,
            'email': contato.email,
            'telefone': contato.telefone,
            'flag': contato.flag
          ##  'contatos': user.contatos[]
    }

    return jsonify(contato = obj)
    
@contato.route('/', methods = ['POST'])
def create():
    body = request.get_json()

    try:
        contato = Contato(email=body['email'], telefone=body['telefone'], flag=body['flag'])

        db.session.add(contato)
        db.session.commit()
        return jsonify(body)
    except Exception as e:
        print('Erro',e)
        return "Server Error", 500

@contato.route('/<int:id>', methods = ['DELETE'])
def delete(id):
    contato = Contato.query.get(id)

    if(contato is None):
        return "Not Found", 404

    db.session.delete(contato)
    db.session.commit()


    return jsonify(contato = id)

@contato.route('/<int:id>', methods = ['PUT'])
def atualizarUsuario(id):
        contato = Contato.query.filter_by(id=id).first();
        body = request.get_json()

        contato.email = body['email'];
        contato.telefone = body['telefone'];
        contato.flag = body['flag'];

        try:
            db.session.add(contato)
            db.session.commit()
            return jsonify(body)
        except Exception as e:
            print('Erro', e)
            return "Server Error", 500
    
@contato.errorhandler(404)
def not_found(error):
    return "Not Found", 404