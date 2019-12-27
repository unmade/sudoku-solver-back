import pytest
from django.urls import reverse
from sudoku import views


@pytest.mark.django_db
def test_daily_sudoku(rf, sudoku_factory):
    sudoku_factory.create_batch(2, is_daily=True)
    url = reverse("daily-sudoku")

    request = rf.get(url)
    response = views.DailySudoku.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_daily_sudoku_no_daily_sudoku_exists(rf):
    url = reverse("daily-sudoku")

    request = rf.get(url)
    response = views.DailySudoku.as_view()(request)

    assert response.status_code == 404


@pytest.mark.django_db
def test_random_sudoku(rf, sudoku_factory):
    sudoku_factory.create_batch(20)
    url = reverse("random-sudoku")

    request = rf.get(url)
    response = views.RandomSudoku.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_random_sudoku_no_sudoku_exists(rf):
    url = reverse("random-sudoku")

    request = rf.get(url)
    response = views.RandomSudoku.as_view()(request)

    assert response.status_code == 404
