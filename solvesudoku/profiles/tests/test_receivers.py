import pytest
from profiles.models import Profile


@pytest.mark.django_db
def test_checks_that_profile_created_for_new_user(django_user_model):
    user = django_user_model.objects.create_user(username="test", password="test")
    profile = Profile.objects.get(user=user)
    assert profile.name == "Anonymous"
    assert profile.picture_url is None
