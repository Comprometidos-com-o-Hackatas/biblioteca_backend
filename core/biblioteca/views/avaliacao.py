from ..models import Avaliacao
from ..serializers import AvaliacaoCreateSerializer, AvaliacaoSerializer
from rest_framework.viewsets import ModelViewSet
import json

class AvaliacaoViewSet(ModelViewSet):
    def get_queryset(self):
        results_param = self.request.query_params.get('results')
        if results_param:
            return Avaliacao.objects.filter(livro=results_param)
        return Avaliacao.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AvaliacaoCreateSerializer
        return AvaliacaoSerializer