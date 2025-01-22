from api.models.contributor import Contributor
from api.models.project import Project
from api.serializers.project_serializer import ProjectDetailSerializer, ProjectListSerializer
from django.db import transaction, IntegrityError
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
        # Récupérer les IDs des projets auxquels l'utilisateur est contributeur
        project_ids = Contributor.objects.filter(user_id=self.request.user).values_list("project_id", flat=True)
        return Project.objects.filter(id__in=project_ids)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            # Assurez que l'utilisateur est bien l'auteur du projet
            request.POST._mutable = True
            request.data["author"] = request.user.pk  # L'ID de l'utilisateur est assigné ici
            request.POST._mutable = False

            # Créer le projet
            project = super(ProjectViewset, self).create(request, *args, **kwargs)

            # Récupérer l'instance du projet créé
            project_instance = Project.objects.get(id=project.data["id"])

            # Créer le contributeur
            Contributor.objects.create(
                user_id=request.user.id, project_id=project_instance.id  # Ajouter l'utilisateur comme contributeur
            )

            # Ajouter l'utilisateur au champ "contributors" du projet
            project_instance.contributors.add(request.user)
            # Sérialisation du projet avec les contributeurs
            serialized_project = ProjectListSerializer(project_instance)

            return Response(serialized_project.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            # Gérer les erreurs d'intégrité (par exemple, des doublons dans les données)
            return Response({"detail": f"Integrity error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Gérer toutes les autres erreurs
            return Response({"detail": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewset, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProjectViewset, self).destroy(request, *args, **kwargs)
