
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User, Product, Review

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)




class Login(Resource):
    def get(self):
        return f'Welcome to the LOGIN route'

api.add_resource(Login,'/login')

class Logout(Resource):
    def get(self):
        return f'Welcome to the LOGOUT route'

api.add_resource(Logout,'/logout')

class Sign_Up(Resource):
    def get(self):
        return f'Welcome to the SIGN_UP route'
api.add_resource(Sign_Up,'/signup')


class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        
        serialized_reviews = [review.to_dict() for review in reviews]
        return make_response(jsonify(serialized_reviews), 200)
    
    def post(self):
        data = request.get_json()
        
        review_text = data['review_text']
    
api.add_resource(Reviews,'/reviews')

class Products(Resource):
    def get(self):
        products = Product.query.all()
        
        serialized_products = [product.to_dict() for product in products]
        return make_response(jsonify(serialized_products), 200)
    
api.add_resource(Products, '/products')    

class ProductById(Resource):
    def get(self, id):
        product = Product.query.get(id)
        
        if  product:
            return jsonify(product.to_dict())
        else:
            return {'error': 'Product not found'}

api.add_resource(ProductById,'/products/<int:id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
