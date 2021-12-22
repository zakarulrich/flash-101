# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

PRODUCTS = {
    1: {'id': 1, 'name': 'Skello'},
    2: {'id': 2, 'name': 'Socialive.tv'},
    3: {'id': 3, 'name': 'Le Wagon'}
}


@app.route('/api/v1/products/<id>', methods=['GET'])
def get_product(id):

    if int(id) in PRODUCTS.keys():
        return PRODUCTS.get(int(id)), 200

    abort(404)


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    products = list(PRODUCTS.values())
    return jsonify(
        products
    ), 200


@app.route('/api/v1/products/<id>', methods=['DELETE'])
def delete_product(id):
    if int(id) in PRODUCTS.keys():
        del PRODUCTS[int(id)]
        return '', 204

    abort(404)


@app.route('/api/v1/products', methods=['POST'])
def create_product():
    START_INDEX = len(PRODUCTS) + 1
    IDENTIFIER_GENERATOR = itertools.count(START_INDEX)
    product = request.get_json()
    product['id'] = next(IDENTIFIER_GENERATOR)
    PRODUCTS[4] = product
    return request.get_json(), 201


@app.route('/api/v1/products/<id>', methods=['PATCH'])
def update_product(id):
    data = request.get_json()
    if data is None or data.get('name') is None:
        abort(400)

    name = data.get('name')
    if(name == ''):
        abort(422)

    if int(id) in PRODUCTS.keys():
        PRODUCTS[int(id)]['name'] = name
        return '', 204

    abort(422)


@ app.route('/')
def hello():
    return "Hello World!"
