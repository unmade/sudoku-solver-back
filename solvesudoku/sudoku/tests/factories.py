import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class SudokuFactory(factory.django.DjangoModelFactory):
    puzzle = (
        "000090100"
        "000002300"
        "007001825"
        "604038900"
        "810000000"
        "009000008"
        "170000600"
        "900010743"
        "403060001"
    )
    box_width = 3
    box_length = 3
    rank = factory.LazyAttribute(lambda x: faker.pyint())

    class Meta:
        model = "sudoku.Sudoku"
