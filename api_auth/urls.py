# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api_auth.views.signup_view import SignupView
from .views import views
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r'users', views.CustomerViewSet)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
] + router.urls