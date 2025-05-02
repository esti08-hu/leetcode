class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        n = len(isConnected)
        parent = [i for i in range(size)]
        rank = [0 for i in range(size)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rank[rx] > rank[ry]:
                    parent[ry] = rx
                elif rank[rx] < rank[ry]:
                    parent[rx] = ry
                else:
                    parent[ry] = rx
                    rank[rx] += 1

        for i in range(size):
            for j in range(i + 1, size): 
                if isConnected[i][j] == 1 and find(i) != find(j) :
                    union(i, j)
                    n -=  1

        return n 