# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.min_heap = []

        def dfs(root):
            if not root:
                return 
            
            if len(self.min_heap) == k:
                heappush(self.min_heap, -root.val)
                heappop(self.min_heap)
            
            else:
                heappush(self.min_heap, -root.val)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return -heappop(self.min_heap)