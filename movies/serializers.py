""" Module serializers """
from re import match
from datetime import timedelta

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

        if Genre.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError('Genre already exists')

        return name

class MovieSerializer(serializers.ModelSerializer):
    """ Serializer of Genre model. """
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            # 'genres',
            'cast',
            'year',
            'user',
            'duration',
            'original_lang',
            'private'
        )
        read_only_fields = ('private', )

    def validate_user(self, user):
        """ Validate user field. """
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            auth_user_id = request.user.id
        else:
            raise serializers.ValidationError("The authenticated user could not be determined.")

        if user and user.id != auth_user_id:
            raise serializers.ValidationError("Invalid user")

        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        duration = rep.pop('duration')

        if duration:
            rep['duration'] = str(timedelta(hours=duration))

        return rep
