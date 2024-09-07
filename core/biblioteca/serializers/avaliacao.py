from ..models import Avaliacao
from rest_framework.serializers import ModelSerializer

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
        depth = 1

class AvaliacaoCreateSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
