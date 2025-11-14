class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}
        q = collections.deque([node])
        clone = Node(node.val)
        visited[node] = clone

        while q:
            curr_node = q.popleft()
            curr_clone = visited[curr_node]
            for nei in curr_node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                
                curr_clone.neighbors.append(visited[nei])
        return clone