from api.models.issues import Issue
from api.serializers.issues_serializer import IssueDetailSerializer, IssueListSerializer
from django.db import transaction
from api.mixins import GetDetailSerializerClassMixin
from rest_framework.viewsets import ModelViewSet
from api.permissions import IssuePermission


class IssuesViewset(GetDetailSerializerClassMixin, ModelViewSet):
    """
    Issue endpoint. Used to get / add / delete issues from a given project.
    Get list / details, Create: Project Contributor or Author
    Update / delete: Issue Author
    """

    permission_classes = (IssuePermission,)

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["projects_pk"])

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        if not request.data.get("assigned_to"):
            request.data["assigned_to"] = request.user.pk
        request.data["project_id"] = self.kwargs["projects_pk"]
        request.POST._mutable = False
        return super(IssuesViewset, self).create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        if not request.data["assigned_to"]:
            request.data["assigned_to"] = request.user.pk
        request.data["project_id"] = self.kwargs["projects_pk"]
        request.POST._mutable = False
        return super(IssuesViewset, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(IssuesViewset, self).destroy(request, *args, **kwargs)
