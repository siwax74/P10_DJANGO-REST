# api/models.py
from django.db import models

from api.models.project import Project
from backend.settings import AUTH_USER_MODEL


class Contributor(models.Model):

    user_id = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("project_id", "user_id")
