from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class MoviesTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.login_user_url = reverse('login-user')
        self.create_user_url = reverse('create-user')
        self.movies_url = reverse('movies-list')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }

        self.movie_body = {
            "title": "V for Vendetta",
            "description": "Movie V for Vendetta",
            "genre": "Action",
            "cast": ["Hugo Weaving", "Natalie Portman"],
            "year": 2005,
            "user": 1,
            "duration": 107,
            "original_lang": "en",
            "director": "James McTeigue",
            "is_private": False
        }
        self.__create_user(self.user_body)
        self.__login_user(self.user_body)

    def __create_user(self, user_body: dict) -> None:
        """ Create user """
        self.client.post(self.create_user_url, user_body, format='json')

    def __login_user(self, user_body: dict) -> None:
        """ Login User """
        response = self.client.post(self.login_user_url, user_body, format='json')
        # Get token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_create_movie_success(self):
        """ Test create movie success"""
        response = self.client.post(self.movies_url, self.movie_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_movie_fail(self):
        """ Test create movie fail """
        response = self.client.post(self.movies_url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_movies(self):
        """ Test get movies """
        self.client.post(self.movies_url, self.movie_body, format='json')
        response = self.client.get(self.movies_url)
        count = response.data.get('count')

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ednpoint_movies_private(self):
        """ Test endpoint movies/private """
        self.movie_body['is_private'] = True
        self.client.post(self.movies_url, self.movie_body, format='json')

        response = self.client.get(f"{self.movies_url}private/")
        is_private =  response.data[0]['is_private']

        self.assertTrue(is_private)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ednpoint_movies_public(self):
        """ Test endpoint movies/public """
        self.client.post(self.movies_url, self.movie_body, format='json')

        response = self.client.get(f"{self.movies_url}public/")
        is_private =  response.data[0]['is_private']

        self.assertFalse(is_private)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie_of_other_user(self):
        """ Test create movie to other user """
        self.client.post(self.movies_url, self.movie_body, format='json')

        self.user_body['email'] = "test_b@gmail.com"
        self.__create_user(self.user_body)

        self.movie_body['user'] = 2
        response = self.client.post(self.movies_url, self.movie_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_movie_of_other_user_with_put(self):
        """ Test update movie of other user with PUT """
        self.client.post(self.movies_url, self.movie_body, format='json')

        self.user_body['email'] = "test_b@gmail.com"
        self.__create_user(self.user_body)

        self.movie_body['user'] = 2
        response = self.client.put(f"{self.movies_url}1/", self.movie_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_movie_of_other_user_with_patch(self):
        """ Test create movie of other user with PATCH"""
        self.client.post(self.movies_url, self.movie_body, format='json')

        self.user_body['email'] = "test_b@gmail.com"
        self.__create_user(self.user_body)

        self.movie_body['user'] = 2
        response = self.client.patch(f"{self.movies_url}1/", self.movie_body, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
