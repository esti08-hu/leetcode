class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n+1)]
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        ans = [0] * n

        for garden in range(1, n+1):
            used  = set()
            for nei in graph[garden]:
                if ans[nei-1] != 0:
                    used.add(ans[nei-1])
            for plant in range(1, 5):
                if plant not in used:
                    ans[garden-1] = plant

        return ans