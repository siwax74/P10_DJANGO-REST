from django.db import models
from backend.settings import AUTH_USER_MODEL

# Types de projet possibles
TYPES = [("BACK-END", "BACK-END"), ("FRONT-END", "FRONT-END"), ("IOS", "IOS"), ("ANDROID", "ANDROID")]


class Project(models.Model):
    """Classe représentant un projet"""

    # Champs du projet
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=2048)
    type_development = models.CharField(choices=TYPES, max_length=12)
    created_time = models.DateTimeField(auto_now_add=True)
    # Relation avec l'auteur du projet (un utilisateur)
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.title
