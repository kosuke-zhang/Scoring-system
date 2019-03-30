from rest_framework.serializers import ModelSerializer

from .models import CompetitionModel


class CompetitionSerializer(ModelSerializer):
    class Meta:
        model = CompetitionModel
        fields = '__all__'
