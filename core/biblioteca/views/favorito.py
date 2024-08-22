from ..models import Favorito
from ..serializers import FavoritoBookSerialializer, FavoritoSerializer
from rest_framework.viewsets import ModelViewSet

class FavoritoViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Favorito.objects.all()
        return Favorito.objects.filter(usuario=self.request.user)
    def get_serializer_class(self):
        if self.action == 'create':
            return FavoritoSerializer
        return FavoritoBookSerialializer