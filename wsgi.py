# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [{'id': 1, 'name': 'Skello'},
            {'id': 2, 'name': 'Socialive.tv'},
            {'id': 3, 'name': 'Le Wagon'}]


@app.route('/api/v1/products/<id>')
def get_product(id):

    for p in PRODUCTS:
        if(p['id'] == int(id)):
            return p

    return jsonify(status_code=404)


@app.route('/api/v1/products')
def get_products():
    return jsonify(
        PRODUCTS
    )


@app.route('/')
def hello():
    return "Hello World!"
