from api.models.issues import Issue
from api.models.project import Project
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.serializers.issues_serializer import IssueListSerializer


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "title", "type_development", "author"]


class ProjectDetailSerializer(ModelSerializer):

    issues = SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type_development", "author", "issues"]

    def get_issues(self, instance):
        queryset = Issue.objects.filter(project_id=instance.id)
        return IssueListSerializer(queryset, many=True).data
