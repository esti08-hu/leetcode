class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) <= 4:
            return "Pending"
        grid = [["", "", ""] for _ in range(3)]

        for i, [r, c] in enumerate(moves):
            if i % 2:
                grid[r][c] = "0"
            else:
                grid[r][c] = "x"
        B_win = ["0", "0", "0"]
        A_win = ["x", "x", "x"]
        # check rows
        for r in range(3):
            if grid[r] == B_win:
                return "B"
            elif grid[r] == A_win:
                return "A"
        
        # check cols
        for c in range(3):
            curr = []
            for r in range(3):
                curr.append(grid[r][c])
            
            if curr == B_win:
                return "B"
            elif curr == A_win:
                return "A"
        
        # check main diag
        diag = []
        for i in range(3):
            diag.append(grid[i][i])

        if diag == B_win:
            return "B"
        elif diag == A_win:
            return "A"
            
        # check sec diag
        diag = []
        j = 0
        for i in range(2, -1, -1):
            diag.append(grid[j][i])
            j += 1
            
        if diag == B_win:
            return "B"
        elif diag == A_win:
            return "A"
        if len(moves) < 9:
            return "Pending"
        return "Draw"