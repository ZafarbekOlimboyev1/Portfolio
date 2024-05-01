from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField, Serializer, EmailField


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class ChangePasswordSerializer(Serializer):
    model = get_user_model()
    old_password = CharField(required=True)
    new_password = CharField(required=True)


class ConfirmEmailSerializer(Serializer):
    model = get_user_model()
    sent_code = CharField(required=True)


class ResetPasswordEmailSerializer(Serializer):
    email = EmailField(required=True)
