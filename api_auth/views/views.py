from rest_framework import viewsets

from api_auth.models.user import Customer
from api_auth.serializers.customer_serializer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer