from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


from bot.models import TgUser
from bot.serializers import TgUserVerCodSerializer


class TgUserUpdate(generics.UpdateAPIView):
    model = TgUser
    serializer_class = TgUserVerCodSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        try:
            user = self.model.objects.get(verification_code=self.request.data.get('verification_code'))
        except self.model.DoesNotExist:
            raise ValidationError({'verification_code': 'Неправильный верификационный код'})

        return user

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class VerificationView(GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        s: TgUserSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)

        tg_user: TgUser = s.validated_data['tg_user']
        tg_user.user = self.request.user
        tg_user.save(update_fields=['user'])
        instance_s: TgUserSerializer = self.get_serializer(tg_user)

        return Response(instance_s.data)