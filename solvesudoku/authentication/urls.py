from rest_social_auth import views as soc_auth_views

from django.urls import re_path

urlpatterns = [
    re_path(
        r"/(?P<provider>[a-zA-Z0-9_-]+)/tokens",
        soc_auth_views.SocialJWTPairOnlyAuthView.as_view(),
        name="social-auth",
    ),
]
