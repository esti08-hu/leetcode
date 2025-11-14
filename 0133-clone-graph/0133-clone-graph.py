class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        
        return dfs(node)