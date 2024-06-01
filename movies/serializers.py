""" Module serializers """
from rest_framework import serializers

from movies.models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    """ Serializer of Genre model. """
    class Meta:
        model = Genre
        fields = ('name', )

class MovieSerializer(serializers.ModelSerializer):
    """ Serializer of Genre model. """
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'genre',
            'cast',
            'year',
            'user',
            'duration',
            'original_lang'
        )
