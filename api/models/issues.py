from django.db import models
from api.models.project import Project
from backend.settings import AUTH_USER_MODEL


class Issue(models.Model):

    # Priorities definition
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )

    # Tags definition
    BUG = 'BUG'
    IMPROVEMENT = 'IMPROVEMENT'
    TASK = 'TASK'
    TAGS_CHOICES = (
        (BUG, 'Bug'),
        (IMPROVEMENT, 'Improvement'),
        (TASK, 'Task')
    )

    # Status definition
    TODO = 'TODO'
    WIP = 'WIP'
    DONE = 'DONE'
    STATUS_CHOICES = (
        (TODO, 'To-do'),
        (WIP, 'WIP'),
        (DONE, 'Done')
    )

    title = models.CharField(max_length=155)
    description = models.CharField(max_length=5000)
    created_time = models.DateTimeField(auto_now_add=True)

    priority = models.CharField(max_length=12, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=12, choices=TAGS_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    author_user_id = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author')

    assignee_user_id = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        related_name='issue_assignee')

    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='issues'
    )