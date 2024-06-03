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

    # Private methods ---------------------------------------------------------
    def __create_user(self, user_body: dict) -> dict:
        """ Create user """
        return self.client.post(self.create_user_url, user_body)

    def __login_user(self, user_body: dict) -> dict:
        """ Login user """
        return self.client.post(self.login_user_url, user_body)


    # Test number Endpoint ----------------------------------------------------
    def test_endpoint_random_number(self):
        """ Test endpoint random number """
        response = self.client.get(reverse('random-number'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Tests register Endpoint -------------------------------------------------
    def test_create_user_with_no_data(self):
        """ Test Create new user with no data """
        response = self.client.post(self.create_user_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_new_user_success(self):
        """ Test Create new user """
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_without_email(self):
        """ Test Create new user without email """
        del self.user_body['email']
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_password(self):
        """ Test Create new user without password """
        del self.user_body['password']
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_same_email(self):
        """ Test Create new user with same email """
        # Create first user
        self.__create_user(self.user_body)

        # Create second user with same email
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_email(self):
        """ Test Create new user with invalid email """
        self.user_body['email'] = 'test'
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_with_less_than_ten_characters(self):
        """ Test Create new user with less than 10 characters """
        self.user_body['password'] = 'TestP@ss'
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_lowercase_character(self):
        """ Test Create new user without one lowercase character """
        self.user_body['password'] = 'TESTP@SSWORD'
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_uppercase_character(self):
        """ Test Create new user without one uppercase character """
        self.user_body['password'] = 'testp@ssword'

        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_without_one_special_character(self):
        """ Test Create new user without one special character """
        self.user_body['password'] = 'TestPassword'
        response = self.__create_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Tests login endpoint ----------------------------------------------------
    def test_login_user_with_no_data(self):
        """ Test Create new user with no data """
        response = self.client.post(self.login_user_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_and_get_access_token_success(self):
        """ Test Login user """
        self.__create_user(self.user_body)
        response = self.__login_user(self.user_body)

        self.assertTrue(response.data.get('access'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_with_invalid_email(self):
        """ Test Login user with invalid email """
        self.user_body['email'] = 'test'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_with_invalid_credentials(self):
        """ Test Login user with invalid credentials """
        self.__create_user(self.user_body)
        self.user_body['password'] = 'TestP@ssword'

        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_user_that_does_not_exist(self):
        """ Test Login with user that does not exist """
        self.user_body['email'] = 'test_other@gmail.com'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_password_with_less_than_ten_characters(self):
        """ Test Create new user with less than 10 characters """
        self.user_body['password'] = 'TestP@ss'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_lowercase_character(self):
        """ Test Create new user without one lowercase character """
        self.user_body['password'] = 'TESTP@SSWORD'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_uppercase_character(self):
        """ Test Create new user without one uppercase character """
        self.user_body['password'] = 'testp@ssword'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_password_without_one_special_character(self):
        """ Test Create new user without one special character """
        self.user_body['password'] = 'TestPassword'
        response = self.__login_user(self.user_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
