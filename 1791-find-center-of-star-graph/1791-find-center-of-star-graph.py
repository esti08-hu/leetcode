class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = [0] * (len(edges)+1)
        for u, v in edges:
            nodes[u-1] += 1
            if nodes[u-1] >= 2:
                return u
            nodes[v-1] += 1
            if nodes[v-1] >= 2:
                return v