# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []

        def dfs(root):
            if not root:
                return
            
            if len(self.heap) == k:
                heappush(self.heap, -root.val)
                heappop(self.heap)
            else:
                heappush(self.heap, -root.val)
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        self.heap.sort()
        
        return -1  * self.heap[0]
