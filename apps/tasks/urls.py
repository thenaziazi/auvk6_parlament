from django.urls import path,include
from apps.tasks.views import EventDetailView, EventDoneView, EventsListView, TaskEditView, TaskStatusUpdateView

urlpatterns = [
    path("events_list/view",EventsListView.as_view(),name="eventslist_view"),
    path("events/<int:event_id>/", EventDetailView.as_view(), name="event_to_organize_detail"),
    path("tasks/<int:task_id>/edit/", TaskEditView.as_view(), name="task_edit"),
    path("tasks/<int:task_id>/status/", TaskStatusUpdateView.as_view(), name="task_status_update"), 
    path('events/<int:event_organized_id>/publish/', EventDoneView.as_view(), name='event_publish'),
]
