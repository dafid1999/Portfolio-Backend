from requests import Response
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from .models import Uzytkownik


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username."""

    username = None
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)

    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username."""

    username = None


class UzytkownikSerializer(serializers.ModelSerializer):
    """Uzytkownik resources serializer."""

    class Meta:
        model = Uzytkownik
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "user_type",
        )
        read_only_fields = ["id"]

    def create(self, validated_data):
        request = self.context.get("request")
        password = validated_data["password"]
        user = Uzytkownik(**validated_data)
        user.set_password(password)
        user.save()
        email = setup_user_email(request, user, [])
        email.verified = True
        email.save()
        return user
