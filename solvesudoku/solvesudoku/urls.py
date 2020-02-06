from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path("shelter/", admin.site.urls),
    path("api/auth", include("authentication.urls")),
    path("api/hints", include("hints.urls")),
    path("api/profiles", include("profiles.urls")),
    path("api/sudoku", include("sudoku.urls")),
]
