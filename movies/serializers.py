""" Module serializers """
from re import match

from rest_framework import serializers

from movies.models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    """ Serializer of Genre model. """
    class Meta:
        model = Genre
        fields = ('name', )

    def validate_name(self, name):
        """ Validate name field. """

        if not match(r'^[A-Za-z\s]+$', name):
            raise serializers.ValidationError('Name must be a string')

        return name

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
