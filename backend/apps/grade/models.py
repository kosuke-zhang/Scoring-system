from django.contrib.auth import get_user_model
from django.db import models

from competition.models import CompetitionModel
from composition.models import CompositionModel

UserModel = get_user_model()


class GradeModel(models.Model):
    score = models.IntegerField('得分')
    composition = models.ForeignKey(CompositionModel, null=False, blank=False, on_delete=models.CASCADE)
    judger = models.ForeignKey(UserModel, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'比赛：{self.composition.competition.name} 作品：{self.composition.name} 得分：{self.judger.name} 评委：{self.judger}'

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = '评分'
