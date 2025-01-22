# api/models.py
from django.db import models

from api.models.project import Project
from backend.settings import AUTH_USER_MODEL


class Contributor(models.Model):
    """Classe représentant un contributeur dans un projet"""

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors_set")

    def __str__(self):
        return f"{self.user} - {self.project.title}"
