from ..serializers import AutoresSerializer
from ..models import Autores
from rest_framework.viewsets import ModelViewSet

class AutoresViewSet(ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer