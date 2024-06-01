from rest_framework import viewsets, permissions

from movies.serializers import MovieSerializer, GenreSerializer
from movies.models import Movie, Genre

class GenresViewSet(viewsets.ModelViewSet):
    """ Genres Viewset """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MoviesViewSet(viewsets.ModelViewSet):
    """ Movies Viewset """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )
