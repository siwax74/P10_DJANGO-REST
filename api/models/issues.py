from django.db import models
from api.models.project import Project
from backend.settings import AUTH_USER_MODEL


class Issue(models.Model):
    """Classe représentant un problème dans un projet"""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    PRIORITY_CHOICES = [(LOW, "Low"), (MEDIUM, "Medium"), (HIGH, "High")]

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"
    ISSUE_TYPE_CHOICES = [(BUG, "Bug"), (FEATURE, "Feature"), (TASK, "Task")]

    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    FINISHED = "Finished"
    STATUS_CHOICES = [(TODO, "To Do"), (IN_PROGRESS, "In Progress"), (FINISHED, "Finished")]

    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="issue_author")
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    issue_type = models.CharField(max_length=10, choices=ISSUE_TYPE_CHOICES, default=TASK)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="issues")
    assigned_to = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
