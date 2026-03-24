from django.contrib import admin
from apps.ministries.models import Ministries, MinistryGoals

@admin.register(Ministries)
class MinistriesAdmin(admin.ModelAdmin):
        list_display = ('id','name','image')
        search_fields = ('name',)
        list_filter = ('id','name',)
        list_display_links = ('id', 'name',)
        ordering = ('id',)

@admin.register(MinistryGoals)
class MinistryGoalsAdmin(admin.ModelAdmin):
        list_display = ('id','name','description','status','ministry',)
        search_fields = ('id','ministry')
        list_filter = ('id','ministry',)
        list_display_links = ('id', 'name','ministry')
        ordering = ('created_at',)