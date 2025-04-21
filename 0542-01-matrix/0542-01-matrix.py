class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        def isBound(r,c):
            return (0 <= r < rows and 0 <= c < cols)

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if isBound(row, col):
                        if mat[row][col]==-1:

                            mat[row][col] = level
                            q.append((row, col))

            level+=1

        return mat