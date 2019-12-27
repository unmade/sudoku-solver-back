from django.urls import path

from . import views

urlpatterns = [
    path("/daily", views.DailySudoku.as_view(), name="daily-sudoku"),
    path("/random", views.RandomSudoku.as_view(), name="random-sudoku"),
]
