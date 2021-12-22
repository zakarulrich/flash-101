# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

PRODUCTS = [{'id': 1, 'name': 'Skello'},
            {'id': 2, 'name': 'Socialive.tv'},
            {'id': 3, 'name': 'Le Wagon'}]


@app.route('/api/v1/products/<id>', methods=['GET'])
def get_product(id):

    for p in PRODUCTS:
        if(p['id'] == int(id)):
            return p, 200

    abort(404)


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(
        PRODUCTS
    ), 200


@app.route('/api/v1/products/<id>', methods=['DELETE'])
def delete_product(id):
    for index, p in enumerate(PRODUCTS):
        if(p['id'] == int(id)):
            del PRODUCTS[index]
            return '', 204

    abort(404)


@app.route('/api/v1/products', methods=['POST'])
def create_product():
    START_INDEX = len(PRODUCTS) + 1
    IDENTIFIER_GENERATOR = itertools.count(START_INDEX)
    product = request.get_json()
    product['id'] = next(IDENTIFIER_GENERATOR)
    PRODUCTS.append(product)
    return request.get_json(), 201


@ app.route('/')
def hello():
    return "Hello World!"
