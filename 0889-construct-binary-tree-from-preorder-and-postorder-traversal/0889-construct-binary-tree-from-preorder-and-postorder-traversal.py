# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, pos):
            if not pre:
                return 


            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root

            left_root = pre[1]
            idx = pos.index(left_root)
            left_size = idx + 1

            root.left = dfs(pre[1: 1+left_size], pos[:left_size])
            root.right = dfs(pre[1+left_size:], pos[left_size: -1])

            return root
        
        return dfs(preorder, postorder)