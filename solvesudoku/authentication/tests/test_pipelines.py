import pytest
from authentication import pipelines
from social_core.backends.google import GoogleOAuth2, GoogleOpenId


@pytest.mark.django_db
def test_update_profile_details(user):
    pipelines.update_profile_details(
        backend=GoogleOAuth2(),
        user=user,
        response={"given_name": "SudokuKid", "picture": "https://path.to/picture.png"},
    )
    assert user.profile.name == "SudokuKid"
    assert user.profile.picture_url == "https://path.to/picture.png"


@pytest.mark.django_db
def test_update_profile_details_but_no_data_provided(user_factory):
    user = user_factory(first_name="")
    pipelines.update_profile_details(
        backend=GoogleOAuth2(), user=user, response={},
    )
    assert user.profile.name == "Anonymous"
    assert user.profile.picture_url is None


@pytest.mark.django_db
def test_update_profile_details_but_with_different_backedn(user_factory):
    user = user_factory(first_name="")
    pipelines.update_profile_details(
        backend=GoogleOpenId(), user=user, response={},
    )
    assert user.profile.name == "Anonymous"
    assert user.profile.picture_url is None
