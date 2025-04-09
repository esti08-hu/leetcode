class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]

        for l, r in dislikes:
            graph[l].append(r)
            graph[r].append(l)

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

        for node in range(1, n+1):
            if node not in colors:
                colors[node] = 0

                if not dfs(node):
                    return False  

        return True
