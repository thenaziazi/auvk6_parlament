from django.urls import path
from apps.ministries import views


urlpatterns = [
    path("ministries_list/", views.ministries_list, name="ministries_list"),
    path("ministries_list/<int:ministry_id>/", views.ministry_detail, name="ministry_detail"),
]