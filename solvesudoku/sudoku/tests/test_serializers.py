from dokusan.entities import Sudoku

from sudoku.serializers import SudokuSerializer


def test_sudoku_serializer():
    data = {
        "cells": [
            {"position": [0, 0, 0], "value": 1, "candidates": []},
            {"position": [0, 1, 0], "value": None, "candidates": [2, 4, 6]},
        ]
    }
    serializer = SudokuSerializer(data=data)
    assert serializer.is_valid(raise_exception=True)
    assert isinstance(serializer.save(), Sudoku)
