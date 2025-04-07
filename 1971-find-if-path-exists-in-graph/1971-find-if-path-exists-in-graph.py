class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)

            for adj in graph[node]:
                if adj not in visited:
                    if dfs(adj):
                        return True
            
            return False
            
        return dfs(source)
            