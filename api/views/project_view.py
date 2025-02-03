from api.models.contributor import Contributor
from api.models.project import Project
from api.serializers.project_serializer import ProjectDetailSerializer, ProjectListSerializer
from django.db import transaction
from rest_framework.response import Response
from api.mixins import GetDetailSerializerClassMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from api.permissions import ProjectPermission


class ProjectViewset(GetDetailSerializerClassMixin, ModelViewSet):
    """
    Project endpoint.
    Create: Anyone
    Get list / details: Contributor or Author
    Update / delete: Author
    """

    permission_classes = (ProjectPermission,)

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        project_ids = Contributor.objects.filter(user_id=self.request.user).values_list("project_id", flat=True)
        if project_ids:
            return Project.objects.filter(id__in=project_ids)
        return Project.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        project = super(ProjectViewset, self).create(request, *args, **kwargs)
        project_id = project.data.get("id")
        contributor = Contributor.objects.create(user_id=request.user.pk, project_id=project_id)
        contributor.save()
        return Response(project.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewset, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProjectViewset, self).destroy(request, *args, **kwargs)
