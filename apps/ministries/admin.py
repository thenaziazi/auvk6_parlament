from django.contrib import admin
from apps.ministries.models import Ministries

@admin.register(Ministries)
class MinistriesAdmin(admin.ModelAdmin):
        list_display = ('id','name','description','image')
        search_fields = ('name',)
        list_filter = ('id','name',)
        list_display_links = ('id', 'name',)
        ordering = ('id',)