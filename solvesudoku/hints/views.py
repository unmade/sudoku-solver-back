from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from sudoku.serializers import SudokuSerializer

from . import solver
from .serializers import HintSerializer


class Hints(APIView):
    def post(self, request, *args, **kwargs):
        sudoku_serializer = SudokuSerializer(data=request.data)
        sudoku_serializer.is_valid(raise_exception=True)
        sudoku = sudoku_serializer.save()
        with_pencil_marking = request.query_params["with_pencil_marks"] == "true"
        try:
            for step in solver.steps(sudoku, with_pencil_marking=with_pencil_marking):
                return Response(HintSerializer(step).data)
        except solver.Unsolvable:
            raise APIException(
                {
                    "title": "Incorrect puzzle",
                    "description": "Please check if your puzzle is correct",
                },
                code=400,
            )
        raise APIException(
            {"title": "Already Solved", "description": "The puzzle is already solved"},
            code=400,
        )
