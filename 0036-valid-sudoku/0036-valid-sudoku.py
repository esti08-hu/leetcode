class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            dig_list = []
            for col in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in dig_list:
                        return False
                    else:
                        dig_list.append(board[row][col])

        for col in range(9):
            dig_list = []
            for row in range(9):
                if board[row][col].isdigit():
                    if board[row][col] in dig_list:
                        return False
                    else:
                        dig_list.append(board[row][col]) 
                        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                dig_list = []
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c].isdigit():
                            if board[r][c] in dig_list:
                                return False
                            else:
                                dig_list.append(board[r][c])

        return True
