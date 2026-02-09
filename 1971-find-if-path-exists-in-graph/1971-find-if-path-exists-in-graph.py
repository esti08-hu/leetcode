class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque({source})
        visited = set({source})
        while q:
            for i in range(len(q)):
                node = q.popleft()

                for nei in graph[node]:
                    if nei == destination:
                        return True

                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
        
        return False
