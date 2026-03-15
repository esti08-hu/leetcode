class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_row = 0
        rook_col = 0

        size = len(board)

        for row in range(size):
            for col in range(size):
                if board[row][col] == "R":
                    rook_row = row
                    rook_col = col
                    break
        powns = 0
        # up
        row = rook_row
        while row >= 0:
            if board[row][rook_col] == "p":
                powns += 1
                break
            if board[row][rook_col] == "B":
                break
            row -= 1
        # down
        row = rook_row
        while row < size:
            if board[row][rook_col] == "p":
                powns += 1
                break
            if board[row][rook_col] == "B":
                break
            row += 1
        
        # right
        col = rook_col
        while col < size:
            if board[rook_row][col] == "p":
                powns += 1
                break
            if board[rook_row][col] == "B":
                break
            col += 1
        
        # left 
        col = rook_col
        while col >= 0:
            if board[rook_row][col] == "p":
                powns += 1
                break
            if board[rook_row][col] == "B":
                break
            col -= 1

        return powns