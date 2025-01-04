from django.test import TestCase
from django.http import HttpRequest
from urllib3 import request

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")