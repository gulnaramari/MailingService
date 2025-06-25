from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для регистрации модели пользователей в админке."""

    list_display = ("id", "username", "email")
