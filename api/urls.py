# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "api"

router = DefaultRouter()
urlpatterns = router.urls  # Inclure toutes les routes générées par le router
