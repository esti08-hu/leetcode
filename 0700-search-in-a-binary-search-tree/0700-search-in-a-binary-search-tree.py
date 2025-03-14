# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def finder(node):
            if not node:
                return None

            if val > node.val:
                return finder(node.right)
            elif val < node.val:
                return finder(node.left)
            else:
                return node

        return finder(root)
        
        