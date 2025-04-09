class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour in colors:
                    if colors[neighbour] == colors[node]:
                        return False
                else:
                    colors[neighbour] = 1 - colors[node]
                    if not dfs(neighbour):
                        return False
            return True 

        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 0
                if not dfs(node):
                    return False  

        return True
