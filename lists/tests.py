from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page(self):
        url = resolve('/')
        self.assertEqual(url.func, home_page)
