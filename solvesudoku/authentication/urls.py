from rest_framework_simplejwt.views import TokenRefreshView
from rest_social_auth import views as soc_auth_views

from django.urls import path, re_path

urlpatterns = [
    re_path(
        r"/(?P<provider>[a-zA-Z0-9_-]+)/tokens",
        soc_auth_views.SocialJWTPairOnlyAuthView.as_view(),
        name="social-auth",
    ),
    path("/tokens/refresh", TokenRefreshView.as_view(), name="refresh-token"),
]
