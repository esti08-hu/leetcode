class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def is_border(row, col):
            return row == 0 or row == rows - 1 or col == 0 or col == cols - 1

        def check(row, col, visited):
            if not inbound(row, col) or board[row][col] == "X" or (row, col) in visited:
                return False 

            if is_border(row, col):
                return True  
                
            visited.add((row, col))

            return check(row + 1, col, visited) or check(row - 1, col, visited) or check(row, col + 1, visited) or check(row, col - 1, visited)


        def dfs(row, col):
            if not inbound(row, col) or board[row][col] != "O":
                return

            board[row][col] = "X" 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    visited = set()
                    if not check(i, j, visited):
                        dfs(i, j)