from dokusan.entities import BoxSize
from dokusan.entities import Sudoku as SudokuGrid

from rest_framework import exceptions, generics

from .filters import RandomSudokuFilter
from .models import Sudoku
from .serializers import SudokuSerializer


class DailySudoku(generics.RetrieveAPIView):
    queryset = Sudoku.objects.daily()
    serializer_class = SudokuSerializer

    def get_object(self):
        queryset = self.get_queryset()
        instance = queryset.first()
        if not instance:
            raise exceptions.NotFound
        return SudokuGrid.from_string(
            instance.puzzle, box_size=BoxSize(instance.box_width, instance.box_length),
        )


class RandomSudoku(generics.RetrieveAPIView):
    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer
    filterset_class = RandomSudokuFilter

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        instance = queryset.random()
        if not instance:
            raise exceptions.NotFound
        return SudokuGrid.from_string(
            instance.puzzle, box_size=BoxSize(instance.box_width, instance.box_length),
        )
