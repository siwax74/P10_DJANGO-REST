from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.models.comment import Comment
from django.urls import reverse


class CommentListSerializer(ModelSerializer):

    issue_url = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "created_time", "description", "author_user_id", "issue_id", "issue_url"]

    def get_issue_url(self, obj):
        project_pk = obj.issue_id.project_id.pk
        issue_pk = obj.issue_id.pk
        return reverse("issues-detail", args=[project_pk, issue_pk])
