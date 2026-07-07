# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        def build(bound):
            if self.idx == len(preorder):
                return None
            if preorder[self.idx] > bound:
                return None
            
            value = preorder[self.idx] 
            self.idx += 1

            root = TreeNode(value)
            
            root.left = build(value)
            root.right = build(bound)

            return root

        return build(float("inf"))