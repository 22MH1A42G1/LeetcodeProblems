class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(i) for i in matrix]