from rest_framework.permissions import BasePermission
from api.models.contributor import Contributor


def check_contributor(user, project_id):
    for contributor in Contributor.objects.filter(project_id=project_id):
        if user == contributor.user_id:
            return True
    return False

class ContributorViewsetPermission(BasePermission):
    """
    Contributors can List other contributors, Read details about them
    Authors can List, Read, Add, Update or Delete a contributor
    """

    message = "You dont have permission to do that."

    def has_permission(self, request, view):
        print(f"Checking global has_permission for user: {request.user}")
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve", "list"]:
            is_contributor = check_contributor(request.user.id, obj)
            print(f"Checking contributor retrieve/list permission for user {request.user}: {is_contributor}")
            return is_contributor
        elif view.action in ["update", "partial_update", "create", "destroy"]:
            is_author = request.user == obj.author
            return is_author


class ProjectPermission(BasePermission):
    """
    Anyone can create a project.
    Authors can Create, Read, Update and Delete a project.
    Contributors can List theirs projects, Read a project.
    """

    message = "You don't have permissions to do that."

    def has_permission(self, request, view):
        if view.action in ["create"]:
            return request.user and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve", "list"]:
            is_contributor = check_contributor(request.user.id, obj)
            return is_contributor
        elif view.action in ["update", "partial_update", "destroy"]:
            is_author = request.user == obj.author
            return is_author
        return True

class IssuePermission(BasePermission):
    """
    Issue author can Update and Delete their issues.
    Project contributors can List all project issues, Read issue or Create issue.
    """
    message = "You don't have permissions to do that."

    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'retrieve']:
            # Lister / crée / détails les issues nécessite que l'utilisateur soit un contributeur du projet
            project_id = view.kwargs.get('projects_pk')
            return check_contributor(request.user, project_id)
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            # Seul l'auteur de l'issue peut la modifier ou la supprimer
            return request.user == obj.author
        return True
