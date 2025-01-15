from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET']) # fonction (FBV, Function-Based View) en une vue DRF
def api_home(request):
    return Response({
        "message": "Bienvenue sur l'API SOFTDESK!",
    })
