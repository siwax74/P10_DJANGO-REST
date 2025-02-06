from rest_framework.serializers import ModelSerializer
from api.models.contributor import Contributor


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id']
