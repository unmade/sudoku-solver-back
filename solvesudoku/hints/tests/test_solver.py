from dokusan.boards import BoxSize, Sudoku

from hints.solver import BulkPencilMarking, PencilMarking


def test_bulk_pencil_marking():
    sudoku = Sudoku.from_list(
        [
            [0, 0, 0, 0, 9, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 2, 3, 0, 0],
            [0, 0, 7, 0, 0, 1, 8, 2, 5],
            [6, 0, 4, 0, 3, 8, 9, 0, 0],
            [8, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 0, 0, 8],
            [1, 7, 0, 0, 0, 0, 6, 0, 0],
            [9, 0, 0, 0, 1, 0, 7, 4, 3],
            [4, 0, 3, 0, 6, 0, 0, 0, 1],
        ],
        box_size=BoxSize(3, 3),
    )

    pencil_marks = BulkPencilMarking(sudoku).first()
    assert len(pencil_marks.changes) == 51
    assert pencil_marks.combination.cells == []


def test_advanced_pencil_marking():
    sudoku = Sudoku.from_list(
        [
            [2, 0, 0, 5, 9, 3, 1, 0, 0],
            [5, 0, 1, 0, 0, 2, 3, 0, 0],
            [3, 9, 7, 6, 4, 1, 8, 2, 5],
            [6, 0, 4, 0, 3, 8, 9, 0, 0],
            [8, 1, 0, 0, 0, 0, 0, 3, 6],
            [7, 3, 9, 0, 0, 6, 0, 0, 8],
            [1, 7, 0, 3, 0, 4, 6, 0, 0],
            [9, 0, 0, 0, 1, 5, 7, 4, 3],
            [4, 0, 3, 0, 6, 0, 0, 0, 1],
        ],
        box_size=BoxSize(3, 3),
    )
    sudoku.update(BulkPencilMarking(sudoku).first().changes)
    # there is a naked pair [7, 8] in the first row at (1, 3) and (1, 4)
    # replace {4, 6, 8} with {4, 8}
    sudoku[1, 1].candidates = {4, 8}

    pencil_marks = PencilMarking(sudoku).first()
    assert len(pencil_marks.changes) == 1
    assert pencil_marks.changes[0].candidates == {4, 6}
    assert pencil_marks.combination.cells == []
