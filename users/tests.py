import unittest
from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestApiSearch(unittest.TestCase):
    def test_api_search_POST(self):
        client = Client()
        url = '/api/search/'
        response = client.post(path=url, data={'api_search':'o'})
        print(response.content)

    def test_api_search_GET(self):
        client = Client()
        url = '/api/search/'
        response = client.get(path=url, data={'api_search':'b'})
        print(response.content)