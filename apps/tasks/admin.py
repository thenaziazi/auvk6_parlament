from django.contrib import admin

from apps.tasks.models import Tasks


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "assigned_to", "ministry", "status", "deadline", "event")
    search_fields = ("name", "assigned_to__username", "event__name", "ministry__name")
    list_filter = ("id", "name", "event", "ministry", "status")
    list_display_links = ("id", "name", "event", "assigned_to")
    ordering = ("-id",)

    fieldsets = (
        ("Поручения", {"fields": ("name",)}),
        ("Описание", {"fields": ("description",)}),
        ("Ответственные", {"fields": ("assigned_to",)}),
        ("Министерство и статус", {"fields": ("ministry", "status")}),
        ("Мероприятие", {"fields": ("event",)}),
        ("Дедлайн", {"fields": ("deadline",)}),
    )
