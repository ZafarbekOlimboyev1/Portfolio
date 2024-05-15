from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField, Serializer


class UserCreateSerializer(ModelSerializer):
    password = CharField(write_only=True, validators=[validate_password])
    default_validators = []

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')


class ChangePasswordSerializer(Serializer):
    model = get_user_model()
    old_password = CharField(required=True)
    new_password = CharField(required=True)