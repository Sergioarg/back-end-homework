from django.db.models import Q

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.permissions import IsOwnerOrReadOnly

class MoviesViewSet(viewsets.ModelViewSet):
    """ Movies Viewset """
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        """ Return movies for the current authenticated user only """
        user = self.request.user

        if user.is_authenticated:
            return Movie.objects.filter(
                Q(is_private=False) | Q(user=user)).order_by('-id')

        public_movies = Movie.objects.filter(is_private=False)
        return public_movies


    @action(detail=False, methods=['GET'])
    def private(self, request) -> Response:
        """ Display movies with private True """
        current_user = request._user
        movies = Movie.objects.filter(
            user=current_user, is_private=True).order_by('-id')

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def public(self, request) -> Response:
        """ Display movies with private False """
        current_user = request._user
        movies = Movie.objects.filter(
            user=current_user, is_private=False).order_by('-id')

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def all(self, request) -> Response:
        """ Display all movies created by the user """
        current_user = request._user
        movies = Movie.objects.filter(user=current_user).order_by('-id')

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
