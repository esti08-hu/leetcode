# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return 
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            val = max(nums)
            root = TreeNode(val)
            idx = nums.index(val)

            root.left = dfs(nums[:idx])
            root.right = dfs(nums[idx+1:])

            return root
        return dfs(nums)