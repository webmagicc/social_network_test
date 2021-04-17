from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, UserLastActivity


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'is_active', 'is_superuser', 'last_login']
    ordering = ('id',)


@admin.register(UserLastActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'created_at')


