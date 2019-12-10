from typing import Iterator, List, Tuple, Type

from dokusan import techniques
from dokusan.entities import Cell, Sudoku
from dokusan.techniques import Combination, Result, Technique


class Unsolvable(Exception):
    pass


class BulkPencilMarking(techniques.PencilMarking):
    def _find(self) -> Iterator[Combination]:
        yield techniques.Combination(name="Pencil Marking", cells=[], values=[])

    def _get_changes(self, combination: Combination) -> List[Cell]:
        bulk = Combination(
            name="",
            cells=[cell for cell in self.sudoku.cells() if not cell.value],
            values=[],
        )
        return super()._get_changes(bulk)


class PencilMarking(Technique):
    def _find(self) -> Iterator[Combination]:
        yield Combination(name="Pencil Marking", cells=[], values=[])

    def _get_changes(self, combination: Combination) -> List[Cell]:
        return [
            cell
            for cell in self._get_correct_cells()
            if cell.candidates - self.sudoku[cell.position[:2]].candidates
        ]

    def _get_correct_cells(self) -> List[Cell]:
        sudoku = Sudoku(*[c for c in self.sudoku.cells() if c.value])
        all_techniques = (
            BulkPencilMarking,
            techniques.NakedPair,
            techniques.NakedTriplet,
            techniques.Omission,
            techniques.XYWing,
            techniques.UniqueRectangle,
        )
        for technique in all_techniques:
            for result in technique(sudoku):
                sudoku.update(result.changes)
        return [cell for cell in sudoku.cells() if cell.candidates]


def steps(sudoku: Sudoku, with_pencil_marking: bool = False) -> Iterator[Result]:
    all_techniques: Tuple[Type[Technique], ...] = (
        techniques.LoneSingle,
        techniques.HiddenSingle,
        techniques.NakedPair,
        techniques.NakedTriplet,
        techniques.Omission,
        techniques.XYWing,
        techniques.UniqueRectangle,
    )
    if with_pencil_marking:
        all_techniques = (BulkPencilMarking, PencilMarking) + all_techniques

    while not sudoku.is_solved():
        for technique in all_techniques:
            try:
                result = technique(sudoku).first()
            except techniques.NotFound:
                continue
            else:
                sudoku.update(result.changes)
                yield result
                break
        raise Unsolvable()
