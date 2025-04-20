class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, word_idx):
            
            if word_idx == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[word_idx]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, word_idx + 1):
                    return True
                
            board[row][col] = temp
            return False
        
        m, n = len(board), len(board[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False