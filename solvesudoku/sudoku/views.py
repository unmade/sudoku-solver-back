from django.shortcuts import get_object_or_404
from dokusan.entities import BoxSize
from dokusan.entities import Sudoku as SudokuGrid
from rest_framework import generics

from .models import Sudoku
from .serializers import SudokuSerializer


class DailySudoku(generics.RetrieveAPIView):
    queryset = Sudoku.objects.daily()
    serializer_class = SudokuSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        return SudokuGrid.from_string(
            obj.puzzle, box_size=BoxSize(obj.box_width, obj.box_length),
        )
