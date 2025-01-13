# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



app_name = "api_auth"

router = DefaultRouter()
router.register(r'users', views.CustomerViewSet)

urlpatterns = [
    path('', include('rest_framework.urls')),
] + router.urls