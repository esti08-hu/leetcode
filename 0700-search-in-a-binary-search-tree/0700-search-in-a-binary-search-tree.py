# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(node):
            while node:
                if val > node.val:
                    node = dfs(node.right)
                elif val < node.val:
                   node = dfs(node.left)
                else:
                    return node

        return dfs(root)
        
        