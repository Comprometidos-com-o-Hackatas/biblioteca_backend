from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UsuarioSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)