from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/sudoku", include("sudoku.urls")),
    path("api/hints", include("hints.urls")),
]
