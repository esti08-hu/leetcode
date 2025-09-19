class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        p_set = set()
        a_set = set()
        
        def dfs(i, j, prev, visited):
            if i <0  or j<0  or i>=rows or j>=cols or (i, j) in visited or heights[i][j] < prev:
                return
            
            visited.add((i, j))
            
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
                
                dfs(ni, nj, heights[i][j], visited)
            
        for i in range(rows):
            dfs(i, 0, -1, p_set)
        for j in range(cols):
            dfs(0, j, -1, p_set)
            
        for i in range(rows):
            dfs(i, cols-1, -1, a_set)
        for j in range(cols):
            dfs(rows-1, j, -1, a_set)
        
        
        return list(p_set & a_set)