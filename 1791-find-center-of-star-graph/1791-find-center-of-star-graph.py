class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(edges) + 1)]

        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        for node, nei in enumerate(graph):
            if len(nei) >= 2:
                return node + 1
