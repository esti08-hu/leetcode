class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        min_score = float('inf')
        visited = set()
        q = deque([1])
        visited.add(1)

        while q:
            node = q.popleft()
            for nb, weight in graph[node]:
                min_score = min(min_score, weight)
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)

        return min_score