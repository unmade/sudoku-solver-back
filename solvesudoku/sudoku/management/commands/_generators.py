from typing import Tuple

from dokusan import exceptions, generators, solvers, stats
from dokusan.boards import Sudoku


def random_sudoku(avg_rank: int = 150) -> Tuple[Sudoku, int]:
    while True:
        sudoku = generators.random_sudoku(avg_rank)
        if (rank := stats.rank(sudoku)) >= avg_rank:
            try:
                list(solvers.steps(sudoku))
            except exceptions.Unsolvable:
                continue
            else:
                return sudoku, rank
