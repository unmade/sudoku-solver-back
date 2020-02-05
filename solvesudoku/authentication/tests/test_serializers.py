import pytest
from authentication.serializers import JWTPairSerializer


@pytest.mark.django_db
def test_token_payload_for_regular_user(user_factory):
    user = user_factory()
    serializer = JWTPairSerializer()
    payload = serializer.get_token_payload(user)
    assert payload == {}


@pytest.mark.django_db
def test_token_payload_for_social_user(user_social_auth_factory):
    social_auth = user_social_auth_factory()
    serializer = JWTPairSerializer()
    payload = serializer.get_token_payload(social_auth.user)
    assert "picture_url" in payload
    assert payload["name"] == social_auth.user.first_name
