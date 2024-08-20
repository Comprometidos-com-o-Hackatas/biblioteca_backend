from rest_framework.viewsets import ModelViewSet
from ..models import Livro
from ..serializers import LivroDetailSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return LivroListSerializer
        return LivroDetailSerializer