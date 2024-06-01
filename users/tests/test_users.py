""" Test Users endpoints  """
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class UsersTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.login_user_url = reverse('login-user')
        self.create_user_url = reverse('create-user')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }

    # Register Path -----------------------------------------------------------
    def test_create_user_with_no_data(self):
        """ Test Create new user with no data """
        response = self.client.post(self.create_user_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_new_user_success(self):
        """ Test Create new user """
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_without_email(self):
        """ Test Create new user without email """
        del self.user_body['email']
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_password(self):
        """ Test Create new user without password """
        del self.user_body['password']
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_same_email(self):
        """ Test Create new user with same email """
        # Create first user
        self.client.post(self.create_user_url, self.user_body)

        # Create second user with same email
        response = self.client.post(self.create_user_url, self.user_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_email(self):
        """ Test Create new user with invalid email """
        self.user_body['email'] = 'test'
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_with_less_than_ten_characters(self):
        """ Test Create new user with less than 10 characters """
        self.user_body['password'] = 'TestP@ss'
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_lowercase_character(self):
        """ Test Create new user without one lowercase character """
        self.user_body['password'] = 'TESTP@SSWORD'
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_uppercase_character(self):
        """ Test Create new user without one uppercase character """
        self.user_body['password'] = 'testp@ssword'

        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_special_character(self):
        """ Test Create new user without one special character """
        self.user_body['password'] = 'TestPassword'
        response = self.client.post(self.create_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test Login --------------------------------------------------------------

    def test_login_user_with_no_data(self):
        """ Test Create new user with no data """
        response = self.client.post(self.login_user_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_success(self):
        """ Test Login user """
        self.client.post(self.create_user_url, self.user_body)
        response = self.client.post(self.login_user_url, self.user_body)

        # token = response.data.get('token')
        # self.assertTrue(token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_login_user_with_invalid_email(self):
        """ Test Login user with invalid email """
        self.user_body['email'] = 'test'
        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_with_invalid_credentials(self):
        """ Test Login user with invalid credentials """
        self.client.post(self.create_user_url, self.user_body)
        self.user_body['password'] = 'TestP@ssword'

        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_user_that_does_not_exist(self):
        """ Test Login with user that does not exist """
        self.user_body['email'] = 'test_other@gmail.com'
        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_password_with_less_than_ten_characters(self):
        """ Test Create new user with less than 10 characters """
        self.user_body['password'] = 'TestP@ss'
        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_lowercase_character(self):
        """ Test Create new user without one lowercase character """
        self.user_body['password'] = 'TESTP@SSWORD'
        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_uppercase_character(self):
        """ Test Create new user without one uppercase character """
        self.user_body['password'] = 'testp@ssword'

        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_special_character(self):
        """ Test Create new user without one special character """
        self.user_body['password'] = 'TestPassword'
        response = self.client.post(self.login_user_url, self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
