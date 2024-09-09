from ..models import Avaliacao
from ..serializers import AvaliacaoCreateSerializer, AvaliacaoSerializer
from rest_framework.viewsets import ModelViewSet
import json

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return AvaliacaoCreateSerializer
        return AvaliacaoSerializer