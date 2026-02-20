# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        self.accum = 0
        def dfs(root):
            if not root:
                return 0

            dfs(root.right)
            self.accum += root.val
            root.val = self.accum
            dfs(root.left)
            return root
        return dfs(root)