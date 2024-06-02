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
    queryset = Movie.objects.filter(private=False).order_by('-id')
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    @action(detail=False, methods=['GET'])
    def private(self, request) -> Response:
        """ Set movie as private """
        current_user = request._user

        movies = Movie.objects.filter(
            user=current_user, private=True).order_by('-id')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def public(self, request) -> Response:
        """ Set movie as private """
        current_user = request._user

        movies = Movie.objects.filter(
            user=current_user, private=False).order_by('-id')
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
