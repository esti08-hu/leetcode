class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        node_list = [1 1 1 1]
        {2: [[1, 1], [3, 1]], 3: [[4, 1]]}
        time = 0 + 1 + 1 + 1 = 3
        q = []
        node = 4
        node_list[node-1] = 1
        check if node in dictioary


        '''
        graph = defaultdict(list)
        for time in times:
            u, v, w = time
            graph[u].append([v, w])
        heap = [(0, k)]
        distances = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in distances:
                continue
            
            distances[node] = time

            for v, w in graph[node]:
                if v not in distances:
                    heapq.heappush(heap, (time + w, v))
        
        if len(distances) != n:
            return -1
        
        return max(distances.values())