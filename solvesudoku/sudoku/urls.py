from django.urls import path

from . import views

urlpatterns = [
    path("", views.DailySudoku.as_view()),
    path("/daily", views.DailySudoku.as_view(), name="daily-sudoku"),
]
