from api.models.comment import Comment
from api.models.issues import Issue
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.serializers.comment_serializer import CommentListSerializer


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            "id",
            "created_time",
            "title",
            "description",
            "priority",
            "issue_type",
            "status",
            "project",
            "assigned_to",
        ]


class IssueDetailSerializer(ModelSerializer):

    comments = SerializerMethodField()

    class Meta:
        model = Issue
        fields = [
            "id",
            "created_time",
            "title",
            "description",
            "priority",
            "issue_type",
            "status",
            "author",
            "assigned_to",
            "project",
            "comments",
        ]

    def get_comments(self, instance):
        queryset = Comment.objects.filter(issue_id=instance.id)
        return CommentListSerializer(queryset, many=True).data
