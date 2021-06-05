from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventsListView.as_view()),
]