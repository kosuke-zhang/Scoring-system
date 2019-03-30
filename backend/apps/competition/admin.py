from django.contrib import admin

from .models import CompetitionModel


class CompetitionAdmin(admin.ModelAdmin):
    fields = ['name', 'judger']
    list_display = ['name']

    list_filter = []
    search_fields = []


admin.site.register(CompetitionModel, CompetitionAdmin)
