from rest_framework.permissions import BasePermission
from api.models.contributor import Contributor
from api.models.project import Project


def check_contributor(user_id, project_id):
    """Vérifie si un utilisateur est contributeur d'un projet"""
    return Contributor.objects.filter(project_id=project_id, user_id=user_id).exists()


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
        print(request.user)
        if view.action in ["create", "list"]:
            return request.user and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve"]:
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

    message = "You dont have permission to do that."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if view.action in ["create", "list"]:
            return check_contributor(request.user, Project.objects.filter(id=view.kwargs["projects_pk"]).first())
        return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action in ["retrieve"]:
            return check_contributor(request.user, obj.project_id)
        elif view.action in ["update", "partial_update", "destroy"]:
            return request.user == obj.author


class CommentPermission(BasePermission):
    """
    Comment author can Update or Delete their comments.
    Project contributors can List all comments of an issue, Read a comment or Create a comment.
    """

    message = "You don't have permission to do that."

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if view.action in ["create", "list"]:
            return check_contributor(request.user, Project.objects.filter(id=view.kwargs["projects_pk"]).first())
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve"]:
            if obj.issue:
                return check_contributor(request.user, obj.issue.project_id)
            return False
        elif view.action in ["update", "partial_update", "destroy"]:
            return request.user == obj.author

        return False
