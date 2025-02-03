from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    """
    Serializer pour gérer la déconnexion en validant le refresh token.
    """

    token = serializers.CharField()

    class Meta:
        fields = ["token"]

    def validate_token(self, value):
        """
        Validation pour vérifier si le jeton passé est un refresh token valide.
        """
        try:
            # Essayer de charger le refresh token
            refresh_token = RefreshToken(value)
        except Exception:
            raise serializers.ValidationError("Le refresh token est invalide ou expiré.")

        # Blacklister le refresh token
        refresh_token.blacklist()

        return value
