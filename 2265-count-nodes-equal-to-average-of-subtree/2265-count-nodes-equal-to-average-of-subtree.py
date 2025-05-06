# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, l_count = dfs(node.left)
            right_sum, r_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = l_count + r_count + 1
            if total_sum // total_count == node.val:
                self.count += 1
            return total_sum, total_count
        self.count = 0
        dfs(root)
        return self.count