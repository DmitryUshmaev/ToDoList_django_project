from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User