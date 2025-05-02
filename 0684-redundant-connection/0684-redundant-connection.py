class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return find(parent[x])
            
        def union(x, y):
            rx = find(x)
            ry = find(y)
            
            if rx != ry:
                if size[rx] > size[ry]:
                    parent[ry] = rx
                    size[rx] += size[ry]
                else:
                    parent[rx] = ry
                    size[ry] += size[rx]
            else: 
                return [x, y]

        for u, v in edges:
            if union(u, v):
                return union(u, v)