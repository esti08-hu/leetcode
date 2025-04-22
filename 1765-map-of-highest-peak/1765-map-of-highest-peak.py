class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])

        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        q = deque()

        height = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    height[i][j] = 0  
                    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inBound(nr, nc) and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))

        return height
