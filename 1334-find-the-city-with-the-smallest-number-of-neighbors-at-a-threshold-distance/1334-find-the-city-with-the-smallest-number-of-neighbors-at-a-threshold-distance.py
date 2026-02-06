class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def get_reachable_count(start_node):
            
            pq = [(0, start_node)]
            
            distances = {i: float('inf') for i in range(n)}
            distances[start_node] = 0
            
            while pq:
                current_dist, u = heapq.heappop(pq)
                
                if current_dist > distances[u]:
                    continue
                
                for v, weight in graph[u]:
                    new_dist = current_dist + weight
                    
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
                        
            count = 0
            for d in distances.values():
                if d <= distanceThreshold:
                    count += 1
            return count

        min_reachable = float('inf')
        best_city = -1
        
        for i in range(n):
            count = get_reachable_count(i)
            
            if count <= min_reachable:
                min_reachable = count
                best_city = i
                
        return best_city