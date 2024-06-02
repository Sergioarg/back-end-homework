from datetime import datetime, timedelta
from requests import get

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, generics
from rest_framework.response import Response

from users.serializers import UserSerializer

class RandomNumberView(APIView):
    """ API endpoint that returns a random number. """

    def get(self, request):
        random_num_api = "http://www.randomnumberapi.com/api/v1.0/random"

        response = get(random_num_api)
        if response.status_code != 200:
            return Response({'Error': "Error to get the API"})

        return Response({'number': response.json()[0]})

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

        serializer = UserSerializer(data=request.data)

        if serializer.validate_password(password):

            user = User.objects.filter(email=email).first()

            if not user:
                response = {"error": "User does not exist."}
                return Response(response, status.HTTP_401_UNAUTHORIZED)

            if user and user.check_password(password):

                token, created = Token.objects.get_or_create(user=user)
                expiration = (datetime.now() + timedelta(minutes=20))
                token.expiration_date = expiration
                token.save()

                return Response({"message": "Logged in successfully.", "token": token.key}, status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials."}, status.HTTP_401_UNAUTHORIZED)
        else:
            errors = serializer.errors
            return Response(errors, status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    # This maybe will not be used
    """ API endpoint that allows users to be viewed or edited. """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
