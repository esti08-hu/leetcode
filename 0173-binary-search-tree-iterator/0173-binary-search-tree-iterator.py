# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.node_list = [root.val] 

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.node_list.append(root.val)
            dfs(root.right)        
        
        dfs(root)
        self.index = 0
        self.length = len(self.node_list)

    def next(self) -> int:
        self.index += 1
        return self.node_list[self.index]

    def hasNext(self) -> bool:
        return self.index+1 < self.length
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()