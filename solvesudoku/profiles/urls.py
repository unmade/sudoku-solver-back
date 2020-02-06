from django.urls import path

from . import views

urlpatterns = [
    path("/me", views.CurrentUserProfile.as_view(), name="current-user-profile"),
]
