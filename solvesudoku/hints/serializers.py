from rest_framework import serializers
from sudoku.serializers import CellSerializer


class CombinationSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(default="")
    values = serializers.ListField(child=serializers.IntegerField())
    cells = CellSerializer(many=True)


class HintSerializer(serializers.Serializer):
    combination = CombinationSerializer()
    changes = CellSerializer(many=True)
