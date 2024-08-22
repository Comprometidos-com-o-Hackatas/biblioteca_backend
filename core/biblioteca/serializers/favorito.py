from ..models import Favorito
from rest_framework.serializers import ModelSerializer

class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class FavoritoBookSerialializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
        depth=2