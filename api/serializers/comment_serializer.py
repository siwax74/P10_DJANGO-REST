from api.models.comment import Comment
from rest_framework.serializers import ModelSerializer


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_time', 'description', 'author_user_id', 'issue_id']