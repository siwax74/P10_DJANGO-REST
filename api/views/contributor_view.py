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
            contributor.user_id for contributor in Contributor.objects.filter(project_id=self.kwargs["projects_pk"])
        ]
        customer = Customer.objects.filter(id__in=cont_usr_ids)
        return customer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # Récupérer le projet et l'utilisateur à partir des données envoyées
        project = Project.objects.filter(id=self.kwargs["projects_pk"]).first()
        user = Customer.objects.filter(username=request.data["username"]).first()
        if Contributor.objects.filter(user_id=user.id, project_id=project.id).exists():
            return Response(
                {"message": "The user is already a contributor for this project."}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            Contributor.objects.create(user_id=user.id, project_id=project.id)
            return Response({"message": "Contributor added successfully!"}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"message": f"Erreur d'intégrité : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        # Récupérer l'ID du projet et de l'utilisateur depuis les paramètres d'URL
        project_id = self.kwargs["projects_pk"]
        user_id = self.kwargs["pk"]
        contributor = Contributor.objects.filter(user_id=user_id, project_id=project_id).first()
        if contributor:
            contributor.delete()
            return Response(data={"success": "Contributor delete to this project!"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data={"Error"}, status=status.HTTP_404_NOT_FOUND)
