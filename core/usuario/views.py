from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all().order_by("id")
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["get", "post", "put", "delete" ])
    def me(self, request):
        user = request.user
        serializer = UsuarioSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)