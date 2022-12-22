from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
