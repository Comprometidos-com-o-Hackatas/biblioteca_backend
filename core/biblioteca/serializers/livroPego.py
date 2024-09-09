from rest_framework.serializers import ModelSerializer
from ..models import LivroPego

class LivroPegoCreateSerializer(ModelSerializer):
    class Meta:
        model = LivroPego
        fields = '__all__'

class LivroPegoSerializer(ModelSerializer):
    class Meta:
        model = LivroPego  
        fields = '__all__'
        depth = 1