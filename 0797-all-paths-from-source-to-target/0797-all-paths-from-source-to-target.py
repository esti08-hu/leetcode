class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        des = len(graph)-1
        def dfs(node, path):
            if node == des:
                res.append(path[:])
                return 
            
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
            return res
        return dfs(0, [0])