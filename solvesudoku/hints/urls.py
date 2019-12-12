from django.urls import path

from . import views

urlpatterns = [
    path("", views.Hints.as_view()),
]
