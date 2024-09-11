from ..models.familia import Familia
from ..serializers.familia import FamiliaSerializer
from rest_framework.viewsets import ModelViewSet

class FamiliaViewSet(ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer