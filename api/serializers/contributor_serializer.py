from rest_framework import serializers
from api.models.contributor import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project"]
