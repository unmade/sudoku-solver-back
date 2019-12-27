import factory
from dokusan import generators
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class SudokuFactory(factory.django.DjangoModelFactory):
    puzzle = factory.LazyAttribute(lambda a: str(generators.random_sudoku(avg_rank=1)))
    box_width = 3
    box_length = 3
    rank = factory.LazyAttribute(lambda x: faker.pyint())

    class Meta:
        model = "sudoku.Sudoku"
