from django.contrib.auth.models import AbstractUser
from django.db import models
from api_auth.models.user_manager import CustomUserManager

class Customer(AbstractUser):

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """
        Returns a string representation of the Customer instance.
        """
        return self.username
