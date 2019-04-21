from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

# Create your models here.

UserModel = get_user_model()


class CompetitionModel(models.Model):
    name = models.CharField('比赛名称', max_length=256, blank=False)
    judger = models.ManyToManyField(UserModel, blank=True)
    date = models.DateField('日期', default=now)

    class Meta:
        verbose_name = '比赛'
        verbose_name_plural = '比赛'

    def __str__(self):
        return self.name
