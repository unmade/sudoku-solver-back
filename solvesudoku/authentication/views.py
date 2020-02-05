from rest_social_auth.views import SocialJWTPairOnlyAuthView

from .serializers import JWTPairSerializer


class SocialAuth(SocialJWTPairOnlyAuthView):
    serializer_class = JWTPairSerializer
