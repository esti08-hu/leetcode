class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] == '.':
                return 
            board[r][c] = "."

            for dr, dc in dir:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        BS = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    dfs(r, c)
                    BS += 1
        return BS
