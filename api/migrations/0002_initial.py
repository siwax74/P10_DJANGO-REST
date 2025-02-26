# Generated by Django 5.1.4 on 2025-02-13 10:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comment_author", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="user_id",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="issue",
            name="assignee_user_id",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_assignee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="issue",
            name="author_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="issue_author", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="issue_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="api.issue"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="author_user_id",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="issue",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="issues", to="api.project"
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="project_id",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.project"),
        ),
        migrations.AlterUniqueTogether(
            name="contributor",
            unique_together={("project_id", "user_id")},
        ),
    ]
