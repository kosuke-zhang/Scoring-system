from django.db import models

from competition.models import CompetitionModel


class CompositionModel(models.Model):
    number = models.IntegerField('编号')
    name = models.CharField('作品名称', max_length=256, blank=False)
    competition = models.ForeignKey(CompetitionModel, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作品'
        verbose_name_plural = '作品'
        unique_together = ("number", "competition")
