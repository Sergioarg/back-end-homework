""" Module serializers """
from datetime import timedelta
from rest_framework import serializers
from rest_framework import status
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """ Serializer of Movie model. """
    cast = serializers.ListField(
        child=serializers.CharField(max_length=50),
        allow_empty=False
    )

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
            'original_lang',
            'is_private',
            'director'
        )

        extra_kwargs = {'user': {'write_only': True}}

    def validate_user(self, user):
        """ Validate user field. """
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            auth_user_id = request.user.id
        else:
            raise serializers.ValidationError(
                "The authenticated user could not be determined.",
                status.HTTP_400_BAD_REQUEST
            )

        if user and user.id != auth_user_id:
            raise serializers.ValidationError(
                "The user must be your current user ID",
                status.HTTP_400_BAD_REQUEST
            )

        return user

    def to_representation(self, instance):
        """ Overwriting representation. """

        rep = super().to_representation(instance)
        duration = rep.pop('duration')

        if duration:
            rep['duration'] = str(timedelta(minutes=duration))
            rep['cast'] = instance.cast

        return rep
