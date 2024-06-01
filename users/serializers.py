""" Module serializers """
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer of django built-in User model. """

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate_email(self, email) -> str:
        """ Validate email. """
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists.")

        return email

    def validate_password(self, password) -> str:
        """ Validate password. """

        if len(password) < 10:
            raise serializers.ValidationError("Password must be at least 10 characters long.")

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")

        if not any(char in "!@?#$&]" for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return password

    def create(self, validated_data):
        """ Create a new user. """

        if not validated_data.get('email'):
            raise serializers.ValidationError("Email is required")

        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email')

        return super().create(validated_data)
