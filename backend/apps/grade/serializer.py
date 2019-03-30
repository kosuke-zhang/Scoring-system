from rest_framework.serializers import ModelSerializer

from .models import GradeModel


class GradeSerializer(ModelSerializer):
    class Meta:
        model = GradeModel
        fields = '__all__'
