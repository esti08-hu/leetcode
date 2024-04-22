class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        queue = collections.deque([('0000', 0)])
        
        while queue:
            node, level = queue.popleft()
            if node == target:
                return level
            
            if node in deadends or node in visited:
                continue
            
            visited.add(node)
            
            for i in range(4):
                digit = int(node[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_node = node[:i] + str(new_digit) + node[i+1:]
                    if new_node not in visited:
                        queue.append((new_node, level + 1))
        
        return -1