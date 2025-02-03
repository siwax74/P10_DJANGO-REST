from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.comment_view import CommentViewset
from api.views.contributor_view import UserContributorsViewset
from api.views.issue_view import IssuesViewset
from rest_framework_nested import routers
from api.views.project_view import ProjectViewset

router = DefaultRouter()  # Définir "projects" URL par Défault
router.register(r"projects/?", ProjectViewset, basename="projects")

issues_router = routers.NestedSimpleRouter(router, r"projects/?", lookup="projects", trailing_slash=False)
issues_router.register(
    r"issues/?",
    IssuesViewset,
    basename="issues",
)

comment_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
comment_router.register(
    r"comments/?",
    CommentViewset,
    basename="comments",
)

users_router = routers.NestedSimpleRouter(router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(
    r"users/?",
    UserContributorsViewset,
    basename="users",
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comment_router.urls)),
    path("", include(users_router.urls)),
]


# ViewSet
# GET /projects/
# POST /projects/
# GET /projects/{id}/
# PUT /projects/{id}/
# DELETE /projects/{id}
