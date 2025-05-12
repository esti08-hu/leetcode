class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]
        cost = 0
        while heap:
            dist, u = heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            cost += dist
            for v in range(n):
                if not visited[v]:
                    heappush(heap, (abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]), v))
        return cost