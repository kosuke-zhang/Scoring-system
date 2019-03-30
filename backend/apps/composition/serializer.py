from rest_framework.serializers import ModelSerializer

from .models import CompositionModel


class CompositionSerializer(ModelSerializer):
    class Meta:
        model = CompositionModel
        fields = '__all__'
