from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class GenresTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.genres_url = reverse('genre-list')
        self.login_user_url = reverse('login-user')
        self.create_user_url = reverse('create-user')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }
        self.genre_body = {
            "name": "Test Genre"
        }

        # Create user
        self.client.post(self.create_user_url, self.user_body)

        # Login user
        user_response = self.client.post(self.login_user_url, self.user_body)
        self.user_token = user_response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token)

        if not User.objects.filter(email=self.user_body['email']).exists():
            self.client.post(self.create_user_url, self.user_body)

    def test_get_genres(self):
        """ Test get genres """
        response = self.client.get(self.genres_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_genre(self):
        """ Test create genre """
        response = self.client.post(self.genres_url, self.genre_body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_genre_without_name(self):
        """ Test create genre without name """
        del self.genre_body['name']
        response = self.client.post(self.genres_url, self.genre_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_genre_with_int_value_in_name(self):
        """ Test create genre with int value in name """

        self.genre_body['name'] = 123
        response = self.client.post(self.genres_url, self.genre_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_genre_with_special_characters(self):
        """ Test create genre with special characters """
        self.genre_body['name'] = 'Test Genre !@#$%^&*()'
        response = self.client.post(self.genres_url, self.genre_body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
