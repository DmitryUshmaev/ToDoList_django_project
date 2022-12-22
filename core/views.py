from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserCreateSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
