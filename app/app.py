from flask import Flask, session, request, make_response, jsonify 
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Product

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class hair_Services(Resource):
    def hair_Services(self):
        return f'Welcome to the hair_Services route'

api.add_resource(hair_Services,'/hair')

class Nail_Bar(Resource):
    def Nail_Bar(self):
        return f'Welcome to the Nail_Bar route'
api.add_resource(Nail_Bar,'/nails')

class Makeup_services(Resource):
    def services(self):
        return f'Welcome to the SERVICES route'

api.add_resource(Makeup_services,'/makeup')

class Product(Resource):
    def products(self):
        return f'Welcome to the PRODUCTS route'

api.add_resource(Product,'/products')

class ProductById(Resource):
    def product(self):
        return f'Welcome to the PRODUCTBYID route'

api.add_resource(ProductById,'/product/<int:id>')

class Login(Resource):
    def login(self):
        return f'Welcome to the LOGIN route'

api.add_resource(Login,'/login')

class Sign_Up(Resource):
    def sign_up(self):
        return f'Welcome to the SIGN_UP route'
api.add_resource(Sign_Up,'/signup')



class Reviews(Resource):
    def reviews(self):
        return f'Welcome to the REVIEWS route'
    
api.add_resource(Reviews,'/reviews')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
