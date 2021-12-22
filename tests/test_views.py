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
        response = self.client.get("/api/v1/products/1000")
        self.assertEquals(response.status_code, 404)

    def test_delete_exist_product(self):
        response = self.client.delete("/api/v1/products/2")
        self.assertEquals(response.status_code, 204)

    def test_create_product(self):
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(
            "/api/v1/products", json={'name': 'HistoVec'}, headers=headers)
        product = response.json
        self.assertTrue("id" in product)
        self.assertTrue("name" in product)
        self.assertEquals(response.status_code, 201)

    def test_update_success_product(self):
        response = self.client.patch(
            "/api/v1/products/1", json={'name': 'SkelloEdit'})
        self.assertIsNone(response.json)
        self.assertEquals(response.status_code, 204)

    def test_update_not_found_product(self):
        response = self.client.patch(
            "/api/v1/products/1000", json={'name': 'SkelloEdit'})
        self.assertEquals(response.status_code, 422)

    def test_update_product_bad_request(self):
        response = self.client.patch(
            "/api/v1/products/1000", json={'x': ''})
        self.assertEquals(response.status_code, 400)
