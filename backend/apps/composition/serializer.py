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


class ListCompositionSerializer(ModelSerializer):
    score_amount = serializers.SerializerMethodField()
    judged_count = serializers.SerializerMethodField()

    class Meta:
        model = CompositionModel
        fields = ["id", "number", "name", "competition", "score_amount", "judged_count"]

    def get_judged_count(self, obj):
        grades = GradeModel.objects.filter(composition=obj.id)
        return grades.count()

    def get_score_amount(self, obj):
        grades = GradeModel.objects.filter(composition=obj.id)
        score_amount = sum([int(i.score) for i in grades])
        return score_amount