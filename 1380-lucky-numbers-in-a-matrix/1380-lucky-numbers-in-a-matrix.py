class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        col_max = set()
        rows = len(matrix)
        cols = len(matrix[0])
        
        for c in range(cols):
            curr = float("-inf")
            for r in range(rows):
                curr = max(curr, matrix[r][c])
            col_max.add(curr)
            
        res = []
        for row in matrix:
            min_val = min(row)
            if min_val in col_max:
                res.append(min_val)
        
        return res