from django.contrib.auth import get_user_model, login, logout
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from core.models import User
from core.serializers import UserRegistrationSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer

USER_MODEL = get_user_model()


class UserRegistrationView(CreateAPIView):
    model = USER_MODEL
    serializer_class = UserRegistrationSerializer


class UserLoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


class ProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = USER_MODEL.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user
