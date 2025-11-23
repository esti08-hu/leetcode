class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        
        ans = float('inf')
        for start in range(n):
            queue = deque([(start, 1 << start, 0)])
            visited = set([(start, 1 << start)])
            
            while queue:
                node, mask, dist = queue.popleft()
                if mask == (1 << n) - 1:
                    ans = min(ans, dist)
                    break
                
                for nei in graph[node]:
                    new_mask = mask | (1 << nei)
                    if (nei, new_mask) not in visited:
                        visited.add((nei, new_mask))
                        queue.append((nei, new_mask, dist + 1))
        
        return ans if ans != float('inf') else -1