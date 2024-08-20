from ..serializers import CategoriaDetailSerializer, CategoriaWriteSerializer
from ..models import Categoria
from rest_framework import viewsets

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategoriaDetailSerializer
        return CategoriaWriteSerializer
    http_method_names = ["get", "post", "put", "delete" ]