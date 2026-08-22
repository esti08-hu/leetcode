class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []

        for row in matrix:
            res.append(sum(row))
        
        return res