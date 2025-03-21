from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        results = []
        
        def dfs(node, level):
            if not node:
                return

            if level >= len(results):
                results.append(deque([]))

            if level % 2 == 0:
                results[level].append(node.val) 
            else:
                results[level].appendleft(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)

        for i, res in enumerate(results):
            results[i] = [*res]

        return results
