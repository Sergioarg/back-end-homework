from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class MoviesTests(APITestCase):
    """ Test Users endpoints """
    def setUp(self):
        self.login_user_url = reverse('login-user')
        self.create_user_url = reverse('create-user')
        self.movies_url = reverse('movie-list')

        self.user_body = {
            "email": "test@gmail.com",
            "password": "TestP@ssword1234",
        }

        self.movie_body = {
            "title": "V for Vendetta",
            "description": "In a futuristic, totalitarian Britain, a freedom fighter known simply as V uses terrorist tactics to fight the oppressive society. Evey aids him in his mission to bring down the fascist government.",
            "cast": "Hugo Weaving, Natalie Portman",
            "year": 2005,
            "user": 1,
            "duration": 2.20,
            "original_lang": "en",
            "genre": "Action/Sci-fi",
            "director": "James McTeigue",
            "private": False
        }

        self.client.post(self.create_user_url, self.user_body, format='json')
        response = self.client.post(self.login_user_url, self.user_body, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

        if not User.objects.filter(id='1').exists():
            self.client.post(self.create_user_url, self.customer_body, format='json')

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
