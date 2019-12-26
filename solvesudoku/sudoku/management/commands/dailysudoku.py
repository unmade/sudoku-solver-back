from django.core.management.base import BaseCommand
from dokusan import stats
from sudoku.models import Sudoku

from . import _generators


class Command(BaseCommand):
    help = "Generates new daily sudoku"

    def add_arguments(self, parser):
        parser.add_argument("--avg-rank", type=int, default=150)

    def handle(self, *args, **options):
        avg_rank = options["avg_rank"]
        sudoku, rank = _generators.random_sudoku(avg_rank)
        Sudoku.objects.create(
            puzzle=str(sudoku),
            box_width=sudoku.box_size.width,
            box_length=sudoku.box_size.length,
            rank=stats.rank(sudoku),
            is_daily=True,
        )
