from django_filters import rest_framework as filters

from .models import Sudoku


class RandomSudokuFilter(filters.FilterSet):
    min_rank = filters.NumberFilter(field_name="rank", lookup_expr="gte")
    max_rank = filters.NumberFilter(field_name="rank", lookup_expr="lte")

    class Meta:
        model = Sudoku
        fields = ["min_rank", "max_rank"]
