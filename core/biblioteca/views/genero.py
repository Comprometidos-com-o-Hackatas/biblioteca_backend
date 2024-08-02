from rest_framework.viewsets import ModelViewSet
from ..models import Generos
from ..serializers import GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GeneroSerializer