from django.urls import reverse


def test_admin_sudoku_changelist(admin_client, sudoku_factory):
    sudoku_factory.create_batch(5)
    url = reverse("admin:sudoku_sudoku_changelist")
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_sudoku_change(admin_client, sudoku_factory):
    sudoku = sudoku_factory.create()
    url = reverse("admin:sudoku_sudoku_change", kwargs={"object_id": sudoku.pk})
    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_sudoku_add(admin_client):
    url = reverse("admin:sudoku_sudoku_add")
    response = admin_client.get(url)
    assert response.status_code == 200
