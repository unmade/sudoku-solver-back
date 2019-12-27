import pytest

from django.core.management import call_command

from sudoku.models import Sudoku


@pytest.mark.django_db
def test_random_sudoku():
    call_command("randomsudoku", total=2, avg_rank=75)
    assert Sudoku.objects.count() == 2
