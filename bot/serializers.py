from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from bot.models import TgUser
from bot.tg import tg_client


class TgUserVerCodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'
        read_only_fields = ('id', 'chat_id', 'user_ud')

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        tg_client.send_message(chat_id=instance.chat_id, text='Успешно')
        return instance


class TgUserSerializer(serializers.ModelSerializer):
    verification_code = serializers.CharField(write_only=True)

    class Meta:
        model = TgUser
        read_only_fields = ('tg_user_id', 'username', 'user_id')
        fields = ('tg_user_id', 'username', 'verification_code', 'user_id')

    def validate(self, attrs):
        verification_code = attrs.get('verification_code')
        tg_user = TgUser.objects.filter(verification_code=verification_code).first()
        if not tg_user:
            raise ValidationError({'verification_code': 'field is incorrect'})
        attrs['tg_user'] = tg_user
        return attrs
