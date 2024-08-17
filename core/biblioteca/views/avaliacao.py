from ..models import Avaliacao
from ..serializers import AvaliacaoCreateSerializer, AvaliacaoSerializer
from rest_framework.viewsets import ModelViewSet

class AvaliacaoViewSet(ModelViewSet):
    def get_queryset(self):
        livro_id = self.request.query_params.get('livro')
        if livro_id:
            return Avaliacao.objects.filter(livro=livro_id)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AvaliacaoCreateSerializer
        return AvaliacaoSerializer