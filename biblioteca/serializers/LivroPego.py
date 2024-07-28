from ..models import LivroPego
from rest_framework.serializers import ModelSerializer

class LivroPegoSerializers(ModelSerializer):
    class Meta:
        model = LivroPego
        fields = '__all__'
        