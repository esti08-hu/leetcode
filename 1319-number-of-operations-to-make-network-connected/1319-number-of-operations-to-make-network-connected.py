class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        graph = [[]*n for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components - 1

