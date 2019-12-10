from rest_framework.exceptions import APIException


class InvalidPuzzle(APIException):
    status_code = 400
    default_detail = {"code": "invalid_puzzle"}


class PuzzleSolved(APIException):
    status_code = 400
    default_detail = {"code": "puzzle_solved"}
