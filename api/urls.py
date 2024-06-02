""" URL configuration for api project. """
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, CreateUserView, LoginView, RandomNumberView
from movies.views import MoviesViewSet, GenresViewSet

# Rest endpoints
router = DefaultRouter()
router.register(r'genres', GenresViewSet, basename='genres')
router.register(r'movies', MoviesViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
    path('random/', RandomNumberView.as_view(), name='random-number'),
    # Users
    path('users/register/', CreateUserView.as_view(), name='create-user'),
    path('users/login/', LoginView.as_view(), name='login-user'),

    path('admin/', admin.site.urls),

]
