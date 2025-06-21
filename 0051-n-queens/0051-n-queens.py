class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        mainDiag = set()
        secDiag = set()

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return res 
            
            for c in range(n):
                if c in col or (r+c) in mainDiag or (r-c) in secDiag:
                    continue
                col.add(c)
                mainDiag.add(r + c)
                secDiag.add(r - c)
                board[r][c] = "Q"
    
                backtrack(r+1)

                col.remove(c)
                mainDiag.remove(r + c)
                secDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
        