class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_not_under_attack(row, col):
            for prev_row in range(row):
                if board[prev_row] == col or \
                   board[prev_row] - prev_row == col - row or \
                   board[prev_row] + prev_row == col + row:
                    return False
            return True

        def place_queen(row):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    board[row] = col
                    place_queen(row + 1)
                    board[row] = -1

        result = []
        board = [-1] * n
        place_queen(0)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]