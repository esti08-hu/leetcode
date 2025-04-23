class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0]) 

        def inBound(r, c):
            return (0<=r<rows and 0<=c<cols)

        cr, cc = click
        if board[cr][cc] == "M":
            board[cr][cc] = "X"
            return board

        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        q = deque()
        q.append((cr,cc))

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                if board[r][c]=="E":
                    board[r][c] = "B"
                    mines = 0
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if inBound(nr,nc):
                            if board[nr][nc] == "M":
                                mines += 1

                    if mines > 0:
                        board[r][c] = str(mines)
                    else:
                        board[r][c] = "B"
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if inBound(nr, nc) and board[nr][nc] == "E":
                                q.append((nr, nc))

        return board
