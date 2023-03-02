import unittest
from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestApiSearch(unittest.TestCase):
    def test_api_search_POST(self):
        client = Client()
        url = '/api/search/'
        response = client.post(path=url, data={'api_search':'o'})
        #print(response.content)

    def test_api_search_GET(self):
        client = Client()
        url = '/api/search/'
        response = client.get(path=url, data={'api_search':'b'})
        #print(response.content)

class TestApiAddProduct(unittest.TestCase):
    def test_api_add_product_POST(self):
        client = Client()
        url = '/api/addproduct/'
        product_data = {
                        'name': 'New product',
                        'price': 20,
                        'description': 'Test product',
                        'category': 2
                        }
        response = client.post(path=url, data=product_data)

class TestApiCategoryProducts(unittest.TestCase):
    def test_api_category_product_GET(self):
        client = Client()
        url = '/api/categoryproduct/'
        response = client.get(path=url, data={'api_category_product': 1})
from django.test import TestCase

# Create your tests here.
