from api.models.contributor import Contributor
from api.models.project import Project
from django.db import transaction, IntegrityError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from api.permissions import ContributorViewsetPermission
from api_auth.models.user import Customer
from api_auth.serializers.customer_serializer import CustomerSerializer


class UserContributorsViewset(ModelViewSet):
    """
    Projects contributor endpoint. Used to get / add / delete contributors from a given project.
    Get returns User objects, so we need to map this viewset to the user model.
    Get list / details: Contributor or Author
    Create / update / delete: Author
    """

    permission_classes = (ContributorViewsetPermission,)

    serializer_class = CustomerSerializer

    def get_queryset(self):
        cont_usr_ids = [
            contributor.user_id.id for contributor in Contributor.objects.filter(project_id=self.kwargs["projects_pk"])
        ]
        return Customer.objects.filter(id__in=cont_usr_ids)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            user_to_add = Customer.objects.filter(username=request.data["username"]).first()
            if user_to_add:
                project = Project.objects.filter(id=self.kwargs["projects_pk"]).first()
                if project:
                    # Vérifier si le contributeur existe déjà pour ce projet
                    existing_contributor = Contributor.objects.filter(
                        user_id=user_to_add.id, project_id=project.id
                    ).first()
                    if existing_contributor:
                        return Response(
                            data={"error": "User is already a contributor for this project!"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                    # Créer un nouveau contributeur
                    contributor = Contributor.objects.create(
                        user_id=user_to_add.id,  # Utilisez l'ID de l'utilisateur
                        project_id=project.id,  # Utilisez l'ID du projet
                    )
                    contributor.save()
                    return Response(data={"Success": "Contributor added to project!"}, status=status.HTTP_201_CREATED)
                return Response(data={"error": "Project does not exist!"}, status=status.HTTP_404_NOT_FOUND)
            return Response(data={"error": "User does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            return Response(
                data={"error": "An integrity error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        user_to_delete = Customer.objects.filter(id=self.kwargs["pk"]).first()
        if user_to_delete == request.user:
            return Response(data={"error": "You cannot delete yourself !"})
        if user_to_delete:
            contributor = Contributor.objects.filter(
                user_id=self.kwargs["pk"], project_id=self.kwargs["projects_pk"]
            ).first()
            if contributor:
                contributor.delete()
                return Response()
            return Response(data={"error": "Contributor not assigned to project !"})
        else:
            return Response(data={"error": "User does not exist !"})
