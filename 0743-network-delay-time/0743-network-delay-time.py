class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in times:
            graph[u-1].append((v-1, w))
            
        min_heap = [(0, k-1)]
        dist = [float("inf")] * n
        dist[k-1] = 0
        
        seen = set()

        while min_heap:
            curr_w, node = heapq.heappop(min_heap)
            if node in seen:
                continue
            seen.add(node)
            for nei, w in graph[node]:
                new_w = curr_w + w
                if dist[nei] > new_w:
                    heapq.heappush(min_heap, (new_w, nei))
                    dist[nei] = new_w
        
        res = max(dist)
        return res if res != float("inf") else -1