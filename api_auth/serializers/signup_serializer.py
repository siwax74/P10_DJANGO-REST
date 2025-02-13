from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import SerializerMethodField, ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    tokens = SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "tokens"]

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            raise ValidationError("User already exists")
        return value

    def validate_password(self, value: str) -> str:
        if value is not None:
            return make_password(value)
        raise ValidationError("Password is empty")

    def get_tokens(self, user: User) -> dict:
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data
