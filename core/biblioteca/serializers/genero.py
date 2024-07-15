from ..models import Generos
from rest_framework.serializers import ModelSerializer

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'