class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                val = board[i][j]
                board[i][j] = [val, val]
        
        dir = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        for i in range(rows):
            for j in range(cols):
                count = 0
                for dr, dc in dir:
                    nr, nc = dr+i, dc+j
                    if inbound(nr, nc):
                        if board[nr][nc][0]:
                            count += 1
                if board[i][j][0]:
                    if count > 3 or count < 2:
                        board[i][j][1] = 0
                else:
                    if count == 3:
                        board[i][j][1] = 1
        for i in range(rows):
            for j in range(cols):
                board[i][j] = board[i][j][1]
        




