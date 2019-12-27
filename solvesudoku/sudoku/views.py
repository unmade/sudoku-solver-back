from dokusan.entities import BoxSize
from dokusan.entities import Sudoku as SudokuGrid
from rest_framework import exceptions, generics

from .models import Sudoku
from .serializers import SudokuSerializer


class DailySudoku(generics.RetrieveAPIView):
    queryset = Sudoku.objects.daily()
    serializer_class = SudokuSerializer

    def get_object(self):
        obj = self.get_queryset().first()
        if not obj:
            raise exceptions.NotFound
        return SudokuGrid.from_string(
            obj.puzzle, box_size=BoxSize(obj.box_width, obj.box_length),
        )


class RandomSudoku(generics.RetrieveAPIView):
    serializer_class = SudokuSerializer

    def get_object(self):
        obj = Sudoku.objects.random()
        if not obj:
            raise exceptions.NotFound
        return SudokuGrid.from_string(
            obj.puzzle, box_size=BoxSize(obj.box_width, obj.box_length),
        )
