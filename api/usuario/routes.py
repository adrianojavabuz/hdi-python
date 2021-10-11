from . import usuario
from flask import request, jsonify
from db import ma, db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from model.Usuario  import Usuario


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
       model = Usuario


usuarios_schema = UsuarioSchema(many=True)

@usuario.route('/', methods = ['GET'])
def findAllContato():
    usuarios = Usuario.query.all()
    res = usuarios_schema.dump(usuarios)
 
    return jsonify(res);

@usuario.route('/usuario/<int:id>', methods = ['GET'])
def findByIdUser(id):
    user = Usuario.query.filter_by(documento=id).first();

    if(user is None):
        return "Not Found", 404

    obj = {
            'id': user.id,
            'nome': user.nome,
            'documento': user.documento,
          ##  'contatos': user.contatos[]
    }

    return jsonify(user = obj)
    
@usuario.route('/usuario', methods = ['POST'])
def create():
    body = request.get_json()

    try:
        user = Usuario(nome=body['nome'], documento=body['documento'])

        db.session.add(user)
        db.session.commit()
        return jsonify(body)
    except Exception as e:
        print('Erro',e)
        return "Server Error", 500

@usuario.route('/usuario/<int:id>', methods = ['DELETE'])
def delete(id):
    user = Usuario.query.get(id)

    if(user is None):
        return "Not Found", 404

    db.session.delete(user)
    db.session.commit()


    return jsonify(user = id)

@usuario.route('/usuario/<int:id>', methods = ['PUT'])
def atualizarUsuario(id):
        user = Usuario.query.filter_by(id=id).first();
        body = request.get_json()
        print(body['documento'])

        user.documento = body['documento'];
        user.nome = body['nome'];

        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(body)
        except Exception as e:
            print('Erro', e)
            return "Server Error", 500
    
@usuario.errorhandler(404)
def not_found(error):
    return "Not Found", 404