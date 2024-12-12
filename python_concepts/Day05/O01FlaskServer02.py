
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'item': '2 litre Bottle', 'price': 120, 'qty': 350},
    'coke': {'item': '500 ml Bottle', 'price': 45, 'qty': 500},
    'thumbs_up': {'item': '300 ml Can', 'price': 60,  'qty': 200}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)
