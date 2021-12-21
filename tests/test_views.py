from flask_testing import TestCase
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2)

    def test_read_exist_product(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        status_code = response.status_code
        self.assertIs(status_code, 200)
        self.assertIs(product['id'], 1)

    def test_read_not_exist_product(self):
        data = self.client.get("/api/v1/products/1000")
        response = data.json
        self.assertEquals(int(response['status_code']), 404)
