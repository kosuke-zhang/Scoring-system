from django.contrib import admin

from .models import CompositionModel


class CompositionAdmin(admin.ModelAdmin):
    fields = ['number', 'name', 'competition']
    list_display = ['number', 'name', 'competition']


admin.site.register(CompositionModel, CompositionAdmin)
