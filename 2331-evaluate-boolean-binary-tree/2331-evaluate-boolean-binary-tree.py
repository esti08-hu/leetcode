# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left:
                return root.val

            val = root.val
            res = 0 if val == 0 else 1
            if val == 2:
                res = dfs(root.left) or dfs(root.right)
            elif val == 3:
                res = dfs(root.left) and dfs(root.right)
            
            return res
        
        return True if dfs(root) == 1 else False
            


