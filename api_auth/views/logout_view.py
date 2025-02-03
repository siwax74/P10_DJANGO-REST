from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extraire le refresh token de la requête
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                # Charger et blacklister le refresh token
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"detail": "Déconnexion réussie, refresh token black-listé."}, status=200)
            except Exception:
                return Response({"detail": "Refresh token invalide ou déjà expiré."}, status=400)

        return Response({"detail": "Refresh token manquant."}, status=400)
