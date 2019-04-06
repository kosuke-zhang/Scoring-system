from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from grade.models import GradeModel
from .models import CompositionModel


class CompositionSerializer(ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = CompositionModel
        fields = ["id", "number", "name", "competition", "score"]

    def get_score(self, obj):
        user = self.context['request'].user.id
        grade = GradeModel.objects.filter(judger=user, composition=obj.id)
        if grade.exists():
            return grade[0].score
        else:
            return False
