from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserRegistrationSerializer

USER_MODEL = get_user_model()


class UserRegistrationView(CreateAPIView):
    model = USER_MODEL
    serializer_class = UserRegistrationSerializer
