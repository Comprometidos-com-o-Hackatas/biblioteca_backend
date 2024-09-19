from ..models import Favorito
from ..serializers import FavoritoBookSerialializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

class FavoritoViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        print(self.request.user)
        if self.request.user:
            return Favorito.objects.filter(usuario=self.request.user)
    def get_serializer_class(self):
        if self.action == 'create':
            return FavoritoSerializer
        return FavoritoBookSerialializer