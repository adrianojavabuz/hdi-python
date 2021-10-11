from flask import Flask
from flask_marshmallow import Marshmallow
import config
from db import db
from  api.contato import contato as contato_blueprint
from  api.usuario import usuario as usuario_blueprint


app = Flask(__name__)
ma = Marshmallow(app)

def config_app(server):
    print('chamou o config')
    server.config['SERVER_NAME'] = config.FLASK_SERVER
    server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

def main():
    config_app(app)

    app.register_blueprint(usuario_blueprint, url_prefix='/api/usuario')
    app.register_blueprint(contato_blueprint, url_prefix='/api/contato')

    db.init_app(app)

    app.run(debug=config.FLASK_DEBUG)

    db.create_all()


if __name__ == '__main__':
    main()