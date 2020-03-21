from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_home_page(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)

    def test_home_page_returns_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, template_name='home.html')
