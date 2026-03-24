from django.urls import path

from apps.events import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index_view"),
    path("events/", views.events_list_public, name="events_list_public"),
    path("events/<int:event_id>/", views.event_detail_public, name="event_detail_public"),
    path("archive/", views.archive_list, name="archive_list"),
    path("archive/<int:event_id>/", views.archive_detail, name="archive_detail"),
    path("plan/", views.year_plan, name="year_plan"),
    path("ministries/", views.ministries_list, name="ministries_list"),
    path("ministries/<int:ministry_id>/", views.ministry_detail, name="ministry_detail"),
]