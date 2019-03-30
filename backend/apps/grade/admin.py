from django.contrib import admin

from .models import GradeModel


class GradeAdmin(admin.ModelAdmin):
    fields = ['score', 'composition', 'judger']
    list_display = ['score', 'composition', 'judger']


admin.site.register(GradeModel, GradeAdmin)
