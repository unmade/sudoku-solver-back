from django.core.management.base import BaseCommand
from dokusan import stats
from sudoku.models import Sudoku

from . import _generators


class Command(BaseCommand):
    help = "Generates and saves to DB sudoku with specified average rank"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=25)
        parser.add_argument("--avg-rank", type=int, default=150)

    def handle(self, *args, **options):
        total, avg_rank = options["total"], options["avg_rank"]
        sudoku_list = [_generators.random_sudoku(avg_rank) for _ in range(total)]
        Sudoku.objects.bulk_create(
            Sudoku(
                puzzle=str(sudoku),
                box_width=sudoku.box_size.width,
                box_length=sudoku.box_size.length,
                rank=stats.rank(sudoku),
            )
            for sudoku, rank in sudoku_list
        )
