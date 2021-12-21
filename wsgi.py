# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1/products')
def get_products():
    product1 = {'id': 1, 'name': 'Skello'}
    product2 = {'id': 2, 'name': 'Socialive.tv'}
    product3 = {'id': 3, 'name': 'Le Wagon'}
    return jsonify(
        product1, product2, product3
    )


@app.route('/')
def hello():
    return "Hello World!"
