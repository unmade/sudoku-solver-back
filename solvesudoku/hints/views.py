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
            for step in solver.steps(sudoku, with_pencil_marking=with_pencil_marking):
                return Response(HintSerializer(step).data)
        except dokusan.exceptions.Unsolvable as exc:
            raise exceptions.InvalidPuzzle from exc
        raise exceptions.PuzzleSolved
