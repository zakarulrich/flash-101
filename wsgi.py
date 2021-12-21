# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1/produits')
def get_products():
    product1 = {'id': 1, 'name': 'Skello'}
    product2 = {'id': 2, 'name': 'Socialive.tv'}
    return jsonify(
        product1, product2
    )


@app.route('/')
def hello():
    return "Hello World!"
