class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    isWater[r][c] = 0
                else:
                    isWater[r][c] = -1
                    
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == len(isWater) or
                        col < 0 or col == len(isWater[0]) or
                        isWater[row][col] != -1):
                        continue
                    isWater[row][col] = level
                    q.append((row, col))
            level+=1
        return isWater
        

