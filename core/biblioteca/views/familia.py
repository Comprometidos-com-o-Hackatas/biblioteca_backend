from ..models.familia import Familia
from ..serializers.familia import FamiliaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

class FamiliaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        user_family = Familia.objects.filter(Usuario = self.request.user)
        if user_family.exists:
            return user_family
        else:
            return None

    serializer_class = FamiliaSerializer

   
    