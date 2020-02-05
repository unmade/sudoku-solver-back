from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        r"/(?P<provider>[a-zA-Z0-9_-]+)/tokens",
        views.SocialAuth.as_view(),
        name="social-auth",
    ),
]
