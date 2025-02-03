from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_auth.serializers.signup_serializer import SignupSerializer
from rest_framework.permissions import AllowAny


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Utilisateur créé avec succès.", "data": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
