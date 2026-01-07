"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            depth += 1
    
        return depth

