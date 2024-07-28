from ..serializers import LivrosListSerializer, LivrosDetailSerializer
from ..models import Livros
from rest_framework.viewsets import ModelViewSet

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return LivrosListSerializer
        return LivrosDetailSerializer