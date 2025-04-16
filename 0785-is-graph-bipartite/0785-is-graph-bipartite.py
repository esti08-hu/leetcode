class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for node in range(len(graph)):
            if node not in color:

                dq = deque([node])
                color[node] = 0  
                
                while dq:
                    node = dq.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[node]
                            dq.append(neighbor)
                        elif color[neighbor] == color[node]:
                            
                            return False
        
        return True