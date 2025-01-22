# accounts/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api_auth.views.logout_view import LogoutView
from api_auth.views.signup_view import SignupView
from .views import views

router = DefaultRouter()
router.register(r"users", views.CustomerViewSet)

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
] + router.urls
