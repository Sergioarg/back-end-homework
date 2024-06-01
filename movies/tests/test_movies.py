from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class MoviesTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.login_user_url = reverse('login-user')
        self.create_user_url = reverse('create-user')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }

    def test_temp(self):
        """ Test Create new user with no data """
        add = lambda x, y: x + y
        self.assertEqual(add(1, 2), 3)

