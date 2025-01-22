from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models.contributor import Contributor
from api.models.project import Project


def check_contributor(user, project):
    for contributor in Contributor.objects.filter(project_id=project.id):
        if user == contributor.user_id:
            return True
    return False


class IsAuthorOrReadOnly(BasePermission):
    """La classe IsAuthorOrReadOnly est une permission personnalisée dans Django REST Framework,
    qui contrôle l'accès des utilisateurs aux ressources selon deux critères principaux :

    Lecture seule pour tous les utilisateurs :
    Les méthodes HTTP considérées comme "sûres" (SAFE_METHODS) permettent à n'importe quel utilisateur d'accéder
    à la ressource sans restrictions. Ces méthodes incluent :

    GET : Récupérer les données.
    HEAD : Récupérer les en-têtes.
    OPTIONS : Obtenir les options disponibles sur une ressource.
    Écriture réservée à l'auteur de la ressource :
    Si la requête tente de modifier les données (par exemple avec les méthodes POST, PUT, PATCH, ou DELETE),
    seule la personne qui a créé la ressource (l'auteur) est autorisée.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ContributorViewsetPermission(BasePermission):
    """
    Contributors can List other contributors, Read details about them
    Authors can List, Read, Add, Update or Delete a contributor
    """

    message = "You dont have permission to do that."

    def has_permission(self, request, view):
        if not request.user and request.user.is_authenticated:
            return False

        if view.action in ["retrieve", "list"]:
            return check_contributor(request.user, Project.objects.filter(id=view.kwargs["projects_pk"]).first())

        elif view.action in ["update", "partial_update", "create", "destroy"]:
            return request.user == Project.objects.filter(id=view.kwargs["projects_pk"]).first().author


class ProjectPermission(BasePermission):
    """
    Anyone can create a project.
    Authors can Create, Read, Update and Delete a project.
    Contributors can List theirs projects, Read a project.
    """

    message = "You don't have permissions to do that."

    def has_permission(self, request, view):
        print(f"Checking global has_permission for user: {request.user}")
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve", "list"]:
            is_contributor = check_contributor(request.user.id, obj)
            print(f"Checking contributor retrieve/list permission for user {request.user}: {is_contributor}")
            return is_contributor
        elif view.action in ["update", "partial_update", "destroy"]:
            is_author = request.user == obj.author
            print(f"Checking author permission for user {request.user}: {is_author}")
            return is_author


class IssuePermission(BasePermission):
    """
    Issue author can Update and Delete their issues.
    Project contributors can List all project issues, Read issue or Create issue.
    """

    message = "You dont have permission to do that."

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action in ["retrieve", "list", "create"]:
            return check_contributor(request.user, obj.project_id)
        elif view.action in ["update", "partial_update", "destroy"]:
            return request.user == obj.author
