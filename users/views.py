from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from rest_framework.views import APIView
from rest_framework import status, permissions, viewsets, generics
from rest_framework.response import Response

from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """ API endpoint that allows users to be created. """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    """ API endpoint that allows users to login. """

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            response = {'error': 'Please provide both email and password.'}
            return Response(response, status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except ValidationError as exc:
            return Response({'error': exc}, status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if not user:
            response = {"error": "User does not exist."}
            return Response(response, status.HTTP_401_UNAUTHORIZED)

        auth_user = authenticate(request, username=user.username, password=password)

        if not auth_user:
            response = {"error": "Invalid credentials."}
            return Response(response, status.HTTP_401_UNAUTHORIZED)

        return Response({"message": "Logged in successfully."})

class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows users to be viewed or edited. """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
