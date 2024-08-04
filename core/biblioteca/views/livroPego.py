from rest_framework.viewsets import ModelViewSet
from ..models import LivroPego
from ..serializers import LivroPegoSerializer

class LivroPegoViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return LivroPego.objects.all()
        return LivroPego.objects.filter(usuario=self.request.user)
    serializer_class = LivroPegoSerializer