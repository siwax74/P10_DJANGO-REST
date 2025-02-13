from api.models.contributor import Contributor
from api.models.project import Project
from django.db import transaction, IntegrityError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from api.permissions import ContributorViewsetPermission
from api_auth.serializers.customer_serializer import CustomerSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


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
        return User.objects.filter(id__in=cont_usr_ids)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            user_to_add = User.objects.filter(email=request.data["email"]).first()
            if user_to_add:
                contributor = Contributor.objects.create(
                    user_id=user_to_add, project_id=Project.objects.filter(id=self.kwargs["projects_pk"]).first()
                )
                contributor.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(data={"error": "User does not exist !"})
        except IntegrityError:
            return Response(data={"error": "User already added !"})

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        user_to_delete = User.objects.filter(id=self.kwargs["pk"]).first()
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
