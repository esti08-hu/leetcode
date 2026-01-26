# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        q = deque({root})
        res = []
        
        while q:
            curr_level = 0
            node_cnt = 0

            for i in range(len(q)):
                node = q.popleft()
                curr_level += node.val
                node_cnt += 1
            
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if node_cnt:
                res.append(curr_level/node_cnt)
        
        return res
                    
