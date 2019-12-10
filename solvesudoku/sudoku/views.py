from dokusan.entities import Sudoku as SudokuGrid
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SudokuSerializer


class Sudoku(APIView):
    def get(self, request, *args, **kwargs):
        sudoku = SudokuGrid.from_list(
            [
                [0, 0, 0, 0, 9, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 2, 3, 0, 0],
                [0, 0, 7, 0, 0, 1, 8, 2, 5],
                [6, 0, 4, 0, 3, 8, 9, 0, 0],
                [8, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 9, 0, 0, 0, 0, 0, 8],
                [1, 7, 0, 0, 0, 0, 6, 0, 0],
                [9, 0, 0, 0, 1, 0, 7, 4, 3],
                [4, 0, 3, 0, 6, 0, 0, 0, 1],
            ]
        )
        return Response(SudokuSerializer(sudoku).data)
