from rest_social_auth.serializers import JWTPairSerializer as JWTPair


class JWTPairSerializer(JWTPair):
    def get_token_payload(self, user):
        payload = super().get_token_payload(user)
        if (social_user := user.social_auth.first()) :
            payload.update(
                {
                    "username": user.username,
                    "name": user.first_name,
                    "picture_url": social_user.extra_data.get("picture"),
                }
            )
        return payload
