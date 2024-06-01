""" Test Users endpoints  """
from rest_framework.test import APITestCase
from django.urls import reverse

class UsersTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.users_url = reverse('user-list')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }

    def test_create_user(self):
        """ Test Create new user """
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 201)

    def test_create_user_without_email(self):
        """ Test Create new user without email """
        del self.user_body['email']
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_create_user_without_password(self):
        """ Test Create new user without password """
        del self.user_body['password']
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_create_user_same_email(self):
        """ Test Create new user with same email """
        # Create first user

        self.client.post(self.users_url, self.user_body)

        # Create second user with same email
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_create_user_with_invalid_email(self):
        """ Test Create new user with invalid email """
        self.user_body['email'] = 'test'
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_password_with_less_than_ten_characters(self):
        """ Test Create new user with less than 10 characters """
        self.user_body['password'] = 'TestP@ss'
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_password_without_one_lowercase_character(self):
        """ Test Create new user without one lowercase character """
        self.user_body['password'] = 'TESTP@SSWORD'
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_password_without_one_uppercase_character(self):
        """ Test Create new user without one uppercase character """
        self.user_body['password'] = 'testp@ssword'
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)

    def test_password_without_one_special_character(self):
        """ Test Create new user without one special character """
        self.user_body['password'] = 'TestPassword'
        response = self.client.post(self.users_url, self.user_body)

        self.assertEqual(response.status_code, 400)
