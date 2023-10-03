from flask import Flask, session, request, make_response, jsonify 
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Product, Order

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


if __name__ == '__main__':
    app.run(debug=True, port=5555)
