from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_home_page(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)

    def test_home_page_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

