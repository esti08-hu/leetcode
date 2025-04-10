class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(node):

            visited.add(node)

            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1 
                
        return count