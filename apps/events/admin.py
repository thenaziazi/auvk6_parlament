from django.contrib import admin
from apps.events.models import Events, EventsToOrganize, EventPhoto, YearPlan

class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 6    

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
        list_display = ('id','name','date','image')
        search_fields = ('name','date')
        list_filter = ('id','name','date')
        list_display_links = ('id', 'name',)
        ordering = ('id',)
        inlines = [EventPhotoInline]

        fieldsets = (
        ('Название мероприятия', {
            'fields': ('name',)
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Дата проведения', {
                'fields': ('date',)
        }),
        ('Картинка', {
                'fields': ('image',)
        })
    )

@admin.register(EventsToOrganize)
class EventToOrganizeAdmin(admin.ModelAdmin):
        list_display = ('id','name','date','image',)
        search_fields = ('name','date',)
        list_filter = ('id','name','date')
        list_display_links = ('id', 'name',)
        ordering = ('id',)

        fieldsets = (
        ('Название мероприятия', {
            'fields': ('name',)
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Дата проведения', {
                'fields': ('date',)
        }),
        ('Картинка', {
                'fields': ('image',)
        }),
    )
   
@admin.register(YearPlan)
class YearPlanAdmin(admin.ModelAdmin):
        list_display = ('id','name','date')
        search_fields = ('id','name','date')
        list_filter = ('id','name','date')
        list_display_links = ('id', 'name',)
        ordering = ('id',)