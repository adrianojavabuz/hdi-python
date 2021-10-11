from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.sansio.response import Response

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/adriano.raggio/Documents/api-flask/db/teste.db"
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(200))
    documento = db.Column(db.Numeric)
    contatos = db.Column(db.BLOB)

    def __init__(self,nome,documento):
        self.nome = nome
        self.documento = documento
       # self.id = id
       # self.contatos = contatos
        

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200))
    telefone = db.Column(db.Numeric)
    flag = db.Column(db.Integer)


@app.route('/usuario', methods = ['GET'])
def findAllUser():
    users = Usuario.query.all()
    json_users = []

    for user in users:
        obj = {
            'id': user.id,
            'nome': user.nome,
            'documento': user.documento,
          ##  'contatos': user.contatos[]
        }
        json_users.append(obj);
    return jsonify(users = json_users);

@app.route('/usuario/<int:id>', methods = ['GET'])
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
    
@app.route('/usuario', methods = ['POST'])
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

@app.route('/usuario/<int:id>', methods = ['DELETE'])
def delete(id):
    user = Usuario.query.get(id)

    if(user is None):
        return "Not Found", 404

    db.session.delete(user)
    db.session.commit()


    return jsonify(user = id)

@app.route('/usuario/<int:id>', methods = ['PUT'])
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
    
@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404