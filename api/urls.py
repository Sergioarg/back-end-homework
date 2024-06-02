""" URL configuration for api project. """
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, CreateUserView, LoginView, RandomNumberView
from movies.views import MoviesViewSet, GenresViewSet

# Rest endpoints
router = DefaultRouter()
router.register(r'genres', GenresViewSet)
router.register(r'movies', MoviesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Users
    path('users/register/', CreateUserView.as_view(), name='create-user'),
    path('random/', RandomNumberView.as_view(), name='random-number'),
    path('users/login/', LoginView.as_view(), name='login-user'),

    path('admin/', admin.site.urls),

]
