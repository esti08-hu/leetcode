# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(node, s, path):
            if not node:
                return 

            curr_sum = s+node.val
            if curr_sum == targetSum and not node.left and not node.right:
                curr_path = path + "," + str(node.val)
                self.res.append(list(map(int, curr_path.strip().split(",")))[1:])
                return

            dfs(node.left, curr_sum, path + "," + str(node.val))
            dfs(node.right, curr_sum, path + "," + str(node.val))

            
        
        dfs(root, 0, "0")
        return self.res
