# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1/products')
def get_products():
    PRODUCTS = {
        1: {'id': 1, 'name': 'Skello'},
        2: {'id': 2, 'name': 'Socialive.tv'},
        3: {'id': 3, 'name': 'Le Wagon'},
    }
    return jsonify(
        PRODUCTS
    )


@app.route('/')
def hello():
    return "Hello World!"
