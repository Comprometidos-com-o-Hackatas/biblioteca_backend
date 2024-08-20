from rest_framework.serializers import ModelSerializer
from ..models import LivroPego

class LivroPegoSerializer(ModelSerializer):
    model = LivroPego  
    fields = ['id', 'livro']
    depth = 1