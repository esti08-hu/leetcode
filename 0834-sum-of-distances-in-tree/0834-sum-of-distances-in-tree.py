class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        count = [1] * n
        res = [0] * n
        
        def dfs_post_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs_post_order(child, node)
                    
                    count[node] += count[child]
                    res[0] += res[child] + count[child]
        
        def dfs_pre_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs_pre_order(child, node)
        
        dfs_post_order(0, -1)
        dfs_pre_order(0, -1)
        
        return res