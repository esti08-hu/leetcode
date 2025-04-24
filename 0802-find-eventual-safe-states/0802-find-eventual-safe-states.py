class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        inDegree = [0]*len(graph)

        for i, nb in enumerate(graph):
            inDegree[i] = len(nb)

        q = deque()
        for i in range(n):
            if inDegree[i] == 0:
                q.append(i)

        adj = {i:[] for i in range(n)}

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
        
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nb in adj[node]:
                inDegree[nb]-=1
                if inDegree[nb] == 0:
                    q.append(nb)
        
        return sorted(order)



