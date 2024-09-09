from rest_framework.viewsets import ModelViewSet
from ..models import LivroPego
from ..serializers import LivroPegoSerializer, LivroPegoCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class LivroPegoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_superuser:
            return LivroPego.objects.all()
        return LivroPego.objects.filter(usuario=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return LivroPegoCreateSerializer
        return LivroPegoSerializer