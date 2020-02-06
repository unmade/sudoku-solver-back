from social_core.backends.google import GoogleOAuth2


def update_profile_details(backend, user, response, *args, **kwargs):
    data = {}

    if isinstance(backend, GoogleOAuth2):
        if response.get("given_name"):
            data["name"] = response["given_name"]
        if response.get("picture"):
            data["picture_url"] = response["picture"]

    if data:
        for key, value in data.items():
            setattr(user.profile, key, value)
        user.profile.save(update_fields=data.keys())
