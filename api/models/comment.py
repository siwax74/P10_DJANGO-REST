from django.db import models
from api.models.issues import Issue
from backend.settings import AUTH_USER_MODEL


class Comment(models.Model):
    """Classe représentant un commentaire pour un problème (issue)"""

    description = models.TextField()
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.issue.title}"
