class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[]*n for _ in range(n)]

        for i, edge in enumerate(edges):
            u, v = edge
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_heap = [(-1.0, start_node)]
        visited = set()
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob *= -1

            if node == end_node:
                return prob
            
            if node in visited:
                continue

            visited.add(node)
            
            for nei, edge_prob in graph[node]:
                if nei not in visited:
                    new_prob = prob * edge_prob
                    heapq.heappush(max_heap, (-new_prob, nei))

        return 0.0