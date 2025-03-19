# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, d):
            if not root:
                return 
            else:
                if d ==len(res):
                    res.append(root.val)
                else:
                    res[d] = max(res[d], root.val)
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        dfs(root, 0)
        return res