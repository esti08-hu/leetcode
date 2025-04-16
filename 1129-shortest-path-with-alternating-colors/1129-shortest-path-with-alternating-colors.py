from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in redEdges:
            adj[src].append((dst, "R"))
        for src, dst in blueEdges:
            adj[src].append((dst, "B"))
            
        q = deque()
        q.append((0, "R"))
        q.append((0, "B"))
        visited = set()
        visited.add((0, "R"))
        visited.add((0, "B"))
        time = 0
        ans = [-1] * n
        ans[0] = 0
        
        while q:
            for i in range(len(q)):
                node, color = q.popleft()
                for neighbour, edgeColor in adj[node]:
                    if (neighbour, edgeColor) not in visited and edgeColor != color:
                        q.append((neighbour, edgeColor))
                        visited.add((neighbour, edgeColor))
                        if ans[neighbour] == -1: 
                            
                            ans[neighbour] = time + 1
            time += 1
        
        return ans