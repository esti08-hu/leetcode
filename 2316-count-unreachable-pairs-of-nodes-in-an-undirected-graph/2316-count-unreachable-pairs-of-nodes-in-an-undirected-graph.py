class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            count = 1

            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei) 

            return count
        component_sizes = []
        for node in range(n):
            if node not in visited:
                size = dfs(node)
                component_sizes.append(size)

        total = 0
        rem = n
        for size in component_sizes:
            rem -= size
            total += size * rem
        return total

