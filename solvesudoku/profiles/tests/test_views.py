import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_me_regular_user(client, user):
    url = reverse("current-user-profile")
    client.force_login(user)
    response = client.get(url)
    assert response.data == {
        "name": user.profile.name,
        "picture_url": None,
    }


@pytest.mark.django_db
def test_me_social_user(client, user_social_auth):
    user = user_social_auth.user
    url = reverse("current-user-profile")
    client.force_login(user)
    response = client.get(url)
    assert response.data == {
        "name": user.profile.name,
        "picture_url": user.profile.picture_url,
    }


@pytest.mark.django_db
def test_me_unauthorized(client):
    url = reverse("current-user-profile")
    response = client.get(url)
    assert response.status_code == 401
