
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

def render_page(request):
    return render(request,'events/events_internal.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.urls')),
    path('tasks/',include('apps.tasks.urls')),
    path('events/',include('apps.events.urls')),
    path('internal/',render_page)
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)