class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows,  cols = len(mat), len(mat[0])
        def check(r, c):
            for i in range(rows):
                if i == r:
                    continue
                if mat[i][c] == 1:
                    return False
            
            for j in range(cols):
                if j == c:
                    continue
                if mat[r][j] == 1:
                    return False
            return True
            
        count = 0 
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    if check(r, c): 
                        count += 1
        
        return count
