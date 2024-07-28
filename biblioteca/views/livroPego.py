from ..models import LivroPego
from ..serializers import LivroPegoSerializers
from rest_framework.viewsets import ModelViewSet

class LivroPegoViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.user != "AnnonimousUser":
            return LivroPego.objects.filter(usuario=self.request.user)
        return LivroPego.objects.all()
    serializer_class = LivroPegoSerializers