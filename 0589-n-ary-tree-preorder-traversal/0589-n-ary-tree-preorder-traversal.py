"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def traverse(root):
            if not root: 
                return
            
            res.append(root.val)

            for c in root.children:
                traverse(c)
        
        traverse(root)
        return res
