from ..models import Autores
from rest_framework.serializers import ModelSerializer

class AutoresSerializer(ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'