class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, i):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in self.seen:
                return False


            if board[r][c] != word[i]:
                return False
            
            if i == len(word)-1:
                return True

            self.seen.add((r, c))

            for dr, dc in dir:
                nr, nc = r + dr, c + dc

                if dfs(nr, nc, i+1):
                    return True
            self.seen.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    self.seen = set()
                    if dfs(r, c, 0):
                        return True

        return False
