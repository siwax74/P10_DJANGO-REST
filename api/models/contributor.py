# api/models.py
from django.db import models

from api.models.project import Project
from backend.settings import AUTH_USER_MODEL

# Rôles possibles des utilisateurs dans un projet
ROLES = [('AUTHOR', 'AUTHOR'), ('CONTRIBUTOR', 'CONTRIBUTOR')]

class Contributor(models.Model):
    """Classe représentant un contributeur à un projet"""

    # Relation avec l'utilisateur (contributeur)
    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Relation avec le projet auquel le contributeur participe
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')
    # Rôle du contributeur dans le projet (parmi les choix définis dans la liste ROLES)
    role = models.CharField(choices=ROLES, max_length=11, default='CONTRIBUTOR')

    class Meta:
        """Définition d'une contrainte d'unicité pour que le même contributeur
           ne puisse pas être associé au même projet plusieurs fois
        """
        unique_together = ('project_id', 'user_id')

    def __str__(self):
        return self.user.username