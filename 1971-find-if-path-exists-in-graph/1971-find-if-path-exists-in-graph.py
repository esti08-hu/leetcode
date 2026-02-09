class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = [False] * n

        def dfs(node):
            if node == destination:
                return True
            seen[node] = True
            res = False
            for nei in graph[node]:
                if not seen[nei]:
                    seen[nei] = True
                    res = res or dfs(nei)
                    
            return res

        return dfs(source)