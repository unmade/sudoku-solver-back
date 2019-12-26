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
