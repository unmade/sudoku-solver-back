import json

import pytest
from django.urls import reverse
from sudoku import serializers, views


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
    sudoku_factory.create_batch(5)
    url = reverse("random-sudoku")

    request = rf.get(url)
    response = views.RandomSudoku.as_view()(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_random_sudoku_rank_filter(rf, sudoku_factory):
    sudoku_factory.create(rank=50)
    sudoku_factory.create(rank=250)
    expected = sudoku_factory.create(rank=150)

    url = reverse("random-sudoku")

    request = rf.get(f"{url}?min_rank=100&max_rank=200")
    response = views.RandomSudoku.as_view()(request)

    content = json.loads(response.rendered_content)
    serializer = serializers.SudokuSerializer(data=content)
    sudoku = serializer.is_valid() and serializer.save()

    assert str(sudoku) == expected.puzzle


@pytest.mark.django_db
def test_random_sudoku_no_sudoku_exists(rf):
    url = reverse("random-sudoku")

    request = rf.get(url)
    response = views.RandomSudoku.as_view()(request)

    assert response.status_code == 404
