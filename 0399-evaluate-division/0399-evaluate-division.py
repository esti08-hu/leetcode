class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        
        graph = defaultdict(dict)
        
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1:
                        return value * result
            return -1
        
        res = []
        for a, b in queries:
            if a in graph and b in graph:
                res.append(dfs(a, b, set()))
            else:
                res.append(-1.0)
        
        return res