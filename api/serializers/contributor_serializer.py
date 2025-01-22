from rest_framework import serializers
from api.models.contributor import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Afficher le nom d'utilisateur

    class Meta:
        model = Contributor
        fields = ["id", "user", "project"]
