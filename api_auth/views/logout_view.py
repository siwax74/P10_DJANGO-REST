from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LogoutView(APIView):
    """
    Vue de déconnexion locale.
    """

    def post(self, request):
        return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
