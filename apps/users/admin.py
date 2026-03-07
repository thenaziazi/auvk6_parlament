from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "ministry",
        "is_staff",
        "is_minister",
        "is_member",
    )
    search_fields = ("username", "email", "first_name", "last_name",)
    list_filter = ("is_staff", "is_superuser", "is_active","is_minister", "is_member" , "ministry")
    fieldsets = UserAdmin.fieldsets + (
        ("Парламент", {"fields": ("ministry",)}),
        ("Доступ", {"fields": ("is_minister","is_member",)})
    )
