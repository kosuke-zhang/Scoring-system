from django.contrib import admin

from .models import UserModel


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'code', 'is_active', 'is_staff']
    list_display = ['username', 'email', 'code', 'is_active', 'is_staff', 'is_superuser']
    readonly_fields = ['code']


admin.site.register(UserModel, UserAdmin)
