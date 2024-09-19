from ..models.blockedBooks import BlockedLivros
from ..serializers.blockedBooks import BlockedBooksSerializer
from rest_framework.viewsets import ModelViewSet

class BlockedBooksViewSet(ModelViewSet):
    queryset = BlockedLivros.objects.all()
    serializer_class = BlockedBooksSerializer