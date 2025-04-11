class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        def dfs(node, visited, ancestors):
            for parent in graph[node]:
                if parent not in visited:
                    visited.add(parent)
                    ancestors.add(parent)
                    dfs(parent, visited, ancestors)
        
        answer = []
        for i in range(n):
            visited = set()
            ancestors = set()
            dfs(i, visited, ancestors)
            answer.append(sorted(ancestors)) 
            
        return answer