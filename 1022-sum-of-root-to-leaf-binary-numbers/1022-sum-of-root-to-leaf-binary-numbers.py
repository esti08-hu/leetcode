# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def preorder(root, curr_val):
            if not root:
                return 
            
            curr_val = curr_val * 10 + root.val

            if not root.left and not root.right:
                self.res += int(str(curr_val), 2)
                return 

            preorder(root.left, curr_val)
            preorder(root.right, curr_val)

        preorder(root, 0)

        return self.res