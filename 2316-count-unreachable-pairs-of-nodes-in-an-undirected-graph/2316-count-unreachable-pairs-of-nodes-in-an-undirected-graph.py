class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            count = 1

            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei)    

            return count
        res = []
        for node in range(n):
            if node not in visited:
                count = dfs(node)
                res.append(count)
                visited.add(node)

        if len(res) == 1:
            return 0
        else:
            total = 0
            rem = n
            for i in res:
                rem -= i
                total += i * rem
        return total

