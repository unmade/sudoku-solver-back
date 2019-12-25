from typing import Tuple

from dokusan import exceptions, generators, solvers, stats
from dokusan.entities import Sudoku


def random_sudoku(avg_rank: int = 150) -> Tuple[Sudoku, int]:
    while True:
        sudoku = generators.random_sudoku(avg_rank)
        rank = stats.rank(sudoku)
        try:
            list(solvers.steps(sudoku))
        except exceptions.Unsolvable:
            continue
        else:
            return sudoku, rank
