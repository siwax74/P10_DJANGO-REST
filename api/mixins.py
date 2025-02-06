class GetDetailSerializerClassMixin:
    """
    Get detail serializer class
    """

    def get_serializer_class(self):
        if (
            self.action == "retrieve"  # Lorsqu'on récupère un objet (GET /objet/{id}/)
            or self.action == "create"  # Lorsqu'on crée un objet (POST /objet/)
            or self.action == "update"  # Lorsqu'on met à jour un objet (PUT/PATCH /objet/{id}/)
            and self.detail_serializer_class is not None  # Si un sérialiseur détaillé est défini
        ):
            return self.detail_serializer_class  # Utilise le sérialiseur détaillé
        return super().get_serializer_class()  # Sinon, utilise le sérialiseur par défaut
