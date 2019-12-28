from dokusan.boards import BoxSize, Cell, Position, Sudoku

from rest_framework import serializers


class CellSerializer(serializers.Serializer):
    position = serializers.ListField(
        child=serializers.IntegerField(), min_length=3, max_length=3
    )
    value = serializers.IntegerField(allow_null=True)
    candidates = serializers.ListField(child=serializers.IntegerField())


class SudokuSerializer(serializers.Serializer):
    cells = CellSerializer(many=True)
    box_size = serializers.ListField(
        child=serializers.IntegerField(), min_length=2, max_length=2, default=[3, 3]
    )

    def create(self, validated_data):
        return Sudoku(
            *[
                Cell(
                    position=Position(*cell["position"]),
                    value=cell["value"],
                    candidates=set(cell["candidates"]),
                )
                for cell in validated_data["cells"]
            ],
            box_size=BoxSize(*validated_data["box_size"]),
        )
