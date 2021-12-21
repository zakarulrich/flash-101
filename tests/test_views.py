from flask_testing import TestCase
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        print(response)
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)
