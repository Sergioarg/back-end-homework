from django.db.models import Q

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from movies.models import Movie, Genre
from movies.serializers import MovieSerializer, GenreSerializer

from movies.permissions import IsOwnerOrReadOnly

class GenresViewSet(viewsets.ModelViewSet):
    """ Genres Viewset """
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MoviesViewSet(viewsets.ModelViewSet):
    """ Movies Viewset """
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        """ Return movies for the current authenticated user only """
        user = self.request.user

        if user.is_authenticated:
            return Movie.objects.filter(Q(private=False) | Q(user=user)).order_by('-id') # .filter(user=user)

        public_movies = Movie.objects.filter(private=False)
        return public_movies


    @action(detail=False, methods=['GET'])
    def private(self, request) -> Response:
        """ Display movies with private True """
        current_user = request._user
        movies = Movie.objects.filter(
            user=current_user, private=True).order_by('-id')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def public(self, request) -> Response:
        """ Display movies with private False """
        current_user = request._user
        movies = Movie.objects.filter(
            user=current_user, private=False).order_by('-id')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
