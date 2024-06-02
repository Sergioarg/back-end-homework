""" Module serializers """
from re import match
from datetime import timedelta

from rest_framework import serializers
from movies.models import Movie

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
            'private',
            'director'
        )

        # extra_kwargs = {'user': {'write_only': True}}

    def validate_user(self, user):
        """ Validate user field. """
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            auth_user_id = request.user.id
        else:
            raise serializers.ValidationError("The authenticated user could not be determined.")

        if user and user.id != auth_user_id:
            raise serializers.ValidationError("User must be your current user id")

        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        duration = rep.pop('duration')

        if duration:
            rep['duration'] = str(timedelta(hours=duration))

        return rep
