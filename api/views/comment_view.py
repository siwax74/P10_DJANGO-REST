from rest_framework import viewsets
from api.models.comment import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
