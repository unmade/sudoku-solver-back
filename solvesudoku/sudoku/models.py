from django.db import models
from django.utils import timezone


class SudokuQuerySet(models.QuerySet):
    def daily(self):
        return self.filter(is_daily=True).order_by("-created_at")


class Sudoku(models.Model):
    puzzle = models.CharField(max_length=255)
    box_width = models.PositiveSmallIntegerField()
    box_length = models.PositiveSmallIntegerField()
    rank = models.PositiveSmallIntegerField()

    is_daily = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = SudokuQuerySet.as_manager()
