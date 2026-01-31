class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        min_heap = [(0, 0, 0)]
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            d, r, c = heapq.heappop(min_heap)

            if r == rows-1 and c == cols-1:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) :
                    nd = max(d, abs(heights[r][c] - heights[nr][nc]))
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(min_heap, (nd, nr, nc))
