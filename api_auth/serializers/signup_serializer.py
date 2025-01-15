from rest_framework import serializers
from datetime import date
from api_auth.models.user import Customer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField

class SignupSerializer(serializers.ModelSerializer):

    tokens = SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['username', 'password', 'date_of_birth', 'can_be_contacted', 'can_data_be_shared', 'tokens']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_date_of_birth(self, value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 15:
            raise serializers.ValidationError("Vous devez avoir plus de 15 ans pour vous inscrire.")
        return value

    def create(self, validated_data):
        # Crée un utilisateur
        user = Customer.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            date_of_birth=validated_data['date_of_birth'],
            can_be_contacted=validated_data['can_be_contacted'],
            can_data_be_shared=validated_data['can_data_be_shared'],
        )
        self.user = user
        return user

    def get_tokens(self, user):
        """Méthode pour obtenir les jetons (tokens) d'authentification pour l'utilisateur"""

        # Générer les jetons à l'aide de Django REST framework simplejwt
        tokens = RefreshToken.for_user(user)
        data = {
            "refresh": str(tokens),  # Convertir le jeton d'actualisation en chaîne
            "access": str(tokens.access_token)  # Convertir le jeton d'accès en chaîne
        }
        # Retourner le dictionnaire contenant les jetons
        return data
