class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        
        for l, r in dislikes:
            graph[l-1].append(r-1)
            graph[r-1].append(l-1)
            
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

        colors = {}

        for node in range(len(graph)):
            if graph[node] and node not in colors:
                colors[node] = 0

                if not dfs(node):
                    return False  

        return True

        