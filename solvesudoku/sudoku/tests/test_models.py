import pytest

from sudoku.models import Sudoku


@pytest.mark.django_db
def test_sudoku_daily_empty_db():
    assert list(Sudoku.objects.daily()) == []


@pytest.mark.django_db
def test_sudoku_daily_returns_last_daily_sudoku(sudoku_factory):
    sudoku_factory.create(is_daily=True)
    daily_sudoku = sudoku_factory.create(is_daily=True)
    assert Sudoku.objects.daily().first() == daily_sudoku


@pytest.mark.django_db
def test_sudoku_random_empty_db():
    assert Sudoku.objects.random() is None


@pytest.mark.django_db
def test_sudoku_random(sudoku_factory):
    sudoku_factory.create(id=1)
    sudoku_factory.create(id=50)
    sudoku_factory.create(id=100)
    assert isinstance(Sudoku.objects.random(), Sudoku)
