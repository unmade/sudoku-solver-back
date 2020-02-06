import json

from dokusan import generators, solvers, techniques
from dokusan.boards import Cell, Position

from django.urls import reverse

from hints import views
from sudoku import serializers


def test_returns_initial_hint(rf):
    sudoku = generators.random_sudoku(avg_rank=1)

    url = f'{reverse("hint")}?with_pencil_marks=true'
    serializer = serializers.SudokuSerializer(sudoku)
    request = rf.post(url, data=serializer.data, content_type="application/json")
    response = views.Hints.as_view()(request)

    content = json.loads(response.rendered_content)
    assert content["combination"]["name"] == "Pencil Marking"
    assert response.status_code == 200


def test_no_hint_without_pencil_marks(rf):
    sudoku = generators.random_sudoku(avg_rank=1)

    url = reverse("hint")
    serializer = serializers.SudokuSerializer(sudoku)
    request = rf.post(url, data=serializer.data, content_type="application/json")
    response = views.Hints.as_view()(request)

    assert response.status_code == 400


def test_returns_hint_for_sudoku_with_pencil_marks(rf):
    sudoku = generators.random_sudoku(avg_rank=1)
    sudoku.update(techniques.BulkPencilMarking(sudoku).first().changes)

    url = reverse("hint")
    serializer = serializers.SudokuSerializer(sudoku)
    request = rf.post(url, data=serializer.data, content_type="application/json")
    response = views.Hints.as_view()(request)

    content = json.loads(response.rendered_content)
    assert content["combination"]["name"] == "Lone Single"
    assert response.status_code == 200


def test_hint_for_invalid_sudoku(rf):
    sudoku = generators.random_sudoku(avg_rank=1)
    sudoku.update(techniques.BulkPencilMarking(sudoku).first().changes)
    sudoku.update(
        [
            Cell(position=Position(0, 0, 0), value=1),
            Cell(position=Position(0, 1, 0), value=1),
        ]
    )

    url = reverse("hint")
    serializer = serializers.SudokuSerializer(sudoku)
    request = rf.post(url, data=serializer.data, content_type="application/json")
    response = views.Hints.as_view()(request)

    content = json.loads(response.rendered_content)
    assert content["code"] == "invalid_puzzle"
    assert response.status_code == 400


def test_hint_for_solved_sudoku(rf):
    sudoku = solvers.backtrack(generators.random_sudoku(avg_rank=1))

    url = reverse("hint")
    serializer = serializers.SudokuSerializer(sudoku)
    request = rf.post(url, data=serializer.data, content_type="application/json")
    response = views.Hints.as_view()(request)

    content = json.loads(response.rendered_content)
    assert content["code"] == "puzzle_solved"
    assert response.status_code == 400
