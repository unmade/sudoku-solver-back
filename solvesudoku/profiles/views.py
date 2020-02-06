from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from . import serializers


class CurrentUserProfile(RetrieveAPIView):
    serializer_class = serializers.ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
