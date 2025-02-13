from django.db import models
from backend.settings import AUTH_USER_MODEL


class Project(models.Model):

    # Projects Types definition
    BACKEND = "BACKEND"
    FRONTEND = "FRONTEND"
    IOS = "IOS"
    ANDROID = "ANDROID"
    TYPES_CHOICES = ((BACKEND, "Back-end"), (FRONTEND, "Front-end"), (IOS, "iOS"), (ANDROID, "Android"))

    title = models.CharField(max_length=155)
    description = models.CharField(max_length=5000)
    type = models.CharField(max_length=12, choices=TYPES_CHOICES)
    author_user_id = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
