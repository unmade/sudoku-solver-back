import dokusan.exceptions

from rest_framework.response import Response
from rest_framework.views import APIView

from sudoku.serializers import SudokuSerializer

from . import exceptions, solver
from .serializers import HintSerializer


class Hints(APIView):
    def post(self, request, *args, **kwargs):
        sudoku_serializer = SudokuSerializer(data=request.data)
        sudoku_serializer.is_valid(raise_exception=True)
        sudoku = sudoku_serializer.save()
        if not sudoku.is_valid():
            raise exceptions.InvalidPuzzle

        with_pencil_marking = request.query_params.get("with_pencil_marks") == "true"
        try:
            step = solver.step(sudoku, with_pencil_marking=with_pencil_marking)
        except dokusan.exceptions.Unsolvable as exc:
            raise exceptions.InvalidPuzzle from exc
        except solver.Solved as exc:
            raise exceptions.PuzzleSolved from exc

        return Response(HintSerializer(step).data)
