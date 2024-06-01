""" URL configuration for api project. """
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, CreateUserView, LoginView

# Rest endpoints
router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Users
    path('users/register/', CreateUserView.as_view(), name='create-user'),
    path('users/login/', LoginView.as_view(), name='login-user'),

    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
