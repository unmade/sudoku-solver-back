from django.urls import path

from . import views

urlpatterns = [
    path("", views.Sudoku.as_view()),
]
