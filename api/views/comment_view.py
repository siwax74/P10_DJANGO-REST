from api.models.comment import Comment
from api.mixins import GetDetailSerializerClassMixin
from rest_framework.viewsets import ModelViewSet
from django.db import transaction
from api.permissions import CommentPermission
from api.serializers.comment_serializer import CommentListSerializer


class CommentViewset(GetDetailSerializerClassMixin, ModelViewSet):
    """
    Issue endpoint. Used to get / add / delete comments from a given issue of a given project.
    Get list / details, Create: Project Contributor or Author
    Update / delete: Comment Author
    """

    permission_classes = (CommentPermission,)

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs["issues_pk"])

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        print("create")
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.data["issue"] = self.kwargs["issues_pk"]
        request.POST._mutable = False
        return super(CommentViewset, self).create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.data["issue_id"] = self.kwargs["issues_pk"]
        request.POST._mutable = False
        return super(CommentViewset, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CommentViewset, self).destroy(request, *args, **kwargs)
