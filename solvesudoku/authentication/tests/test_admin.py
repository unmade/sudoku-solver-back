from django.urls import reverse


def test_admin_user_changelist(admin_client, user_factory):
    user_factory.create_batch(5)
    url = reverse("admin:authentication_user_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_user_change(admin_client, user_factory):
    user = user_factory.create()
    url = reverse("admin:authentication_user_change", kwargs={"object_id": user.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_user_add(admin_client):
    url = reverse("admin:authentication_user_add")
    response = admin_client.get(url)
    assert response.status_code == 403
