from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.models import User

USER_MODEL = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def create(self, validated_data) -> USER_MODEL:
        password = validated_data.get('password')
        password_repeat = validated_data.pop('password_repeat')

        if password != password_repeat:
            raise serializers.ValidationError('Passwords don`t match')

        hashed_password = make_password(password)
        validated_data['password'] = hashed_password
        instance = super().create(validated_data)
        return instance

    class Meta:

        model = USER_MODEL
        fields = '__all__'
