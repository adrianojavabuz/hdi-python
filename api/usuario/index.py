from flask import Blueprint, jsonify
from flask_sqlalchemy import model
from config import ma
from model.Usuario import Usuario

usuario = Blueprint('usuario', __name__)

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
       model = Usuario

usuarios_schema = UsuarioSchema(many=True)

@usuario.route('/', methods=['GET'])
def main():
    return 'teste'

@usuario.route('/usuario', methods = ['GET'])
def findAllUser():
    users = Usuario.query.all()
    res = usuarios_schema.dump(users)
  #  json_users = []

 
    return jsonify(res);