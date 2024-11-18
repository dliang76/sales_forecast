from django.test import TestCase
from ninja.testing import TestClient
from .api import router

# Create your tests here.
class statusTest(TestCase):
    def test_status(self):
        client = TestClient(router)
        response = client.get("/status")
        print(response)

        self.assertEqual(response.status_code, 200) # check status
        self.assertEqual(response.content, b"API running...") # check message

class predictTest(TestCase):
    def test_predict(self):
        client = TestClient(router)
        response = client.post("/predict", json = {'date':'2024-01-31', 'store': 1, 'item': 1})

        self.assertEqual(response.status_code, 200) # check status
        self.assertEqual(response.content, b'{"sales": 17.08}') # check result
