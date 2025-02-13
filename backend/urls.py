from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),  # exemple : http://127.0.0.1:8000/api/
    path("api/auth/", include("api_auth.urls")),  # Example: http://127.0.0.1:8000/api/auth/login
    path(
        "api-auth/", include("rest_framework.urls")
    ),  # Example: http://127.0.0.1:8000/api-auth/login pour formulaire Django
]
