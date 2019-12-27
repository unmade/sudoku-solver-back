import random

from django.db import models
from django.utils import timezone


class SudokuQuerySet(models.QuerySet):
    def daily(self):
        return self.filter(is_daily=True).order_by("-created_at")

    def random(self):
        minmax = self.aggregate(min_id=models.Min("id"), max_id=models.Max("id"))
        min_id, max_id = minmax["min_id"], minmax["max_id"]
        if min_id is None or max_id is None:
            return None

        while True:
            pk = random.randint(min_id, max_id)
            if sudoku := self.filter(pk=pk).first():
                return sudoku


class Sudoku(models.Model):
    puzzle = models.CharField(max_length=255)
    box_width = models.PositiveSmallIntegerField()
    box_length = models.PositiveSmallIntegerField()
    rank = models.PositiveSmallIntegerField()

    is_daily = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = SudokuQuerySet.as_manager()
