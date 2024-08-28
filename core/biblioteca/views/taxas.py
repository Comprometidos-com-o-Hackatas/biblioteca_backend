from rest_framework import viewsets
from core.biblioteca.models import Taxas
from core.biblioteca.serializers import TaxaSerializer

class TaxasViewSet(viewsets.ModelViewSet):
    queryset = Taxas.objects.all()
    serializer_class = TaxaSerializer