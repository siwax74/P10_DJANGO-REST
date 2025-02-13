from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from api_auth.models.user_manager import CustomUserManager


class Customer(AbstractUser, PermissionsMixin):

    username = None
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    can_be_contacted = models.BooleanField(default=True)  # Peut être contacté
    can_data_be_shared = models.BooleanField(default=False)  # Peut-on partager ses données
    date_of_birth = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        """Méthode pour vérifier si l'utilisateur a une permission particulière"""
        return True

    def has_module_perms(self, app_label):
        """Méthode pour vérifier si l'utilisateur a des permissions pour un module d'application"""
        return True
