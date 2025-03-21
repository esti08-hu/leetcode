"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def traverse(root):
            if not root:
                return
            
            for c in root.children:
                traverse(c)
            
            res.append(root.val)
        

        res = []
        traverse(root)
        return res