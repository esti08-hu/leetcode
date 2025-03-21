"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        dq = deque([root])

        res = []

        while dq:
            level = []
            l = len(dq)
            for _ in range(l):
                node = dq.popleft()

                level.append(node.val)

                for c in node.children:
                    dq.append(c)
            res.append(level)
        return res