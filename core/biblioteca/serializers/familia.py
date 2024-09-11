from core.biblioteca.models.familia import Familia
from rest_framework.serializers import ModelSerializer

class FamiliaSerializer(ModelSerializer):
    class Meta:
        model = Familia
        fields = "__all__"
        depth = 1