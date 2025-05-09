class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        graph = defaultdict(list)
        indegree = {}
        
        for i in range(rows):
            for j in range(cols):
                indegree[(i, j)] = 0
                
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                        graph[(i, j)].append((ni, nj))
                        indegree[(ni, nj)] += 1
        
        queue = deque([(i, j) for i in range(rows) for j in range(cols) if indegree[(i, j)] == 0])
        path_length = 0
        
        while queue:
            path_length += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ni, nj in graph[(i, j)]:
                    indegree[(ni, nj)] -= 1
                    if indegree[(ni, nj)] == 0:
                        queue.append((ni, nj))
                        
        return path_length