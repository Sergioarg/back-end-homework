""" Module serializers """
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer of django built-in User model. """

    class Meta:
        model = User
        fields = ('email', 'password')
