class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def dfs(node, path):
            if not node:
                return
                
            path.append(chr(node.val + ord('a')))
            
            if not node.left and not node.right:
                path_str = ''.join(reversed(path))
                if not self.smallest or path_str < self.smallest:
                    self.smallest = path_str
            
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()

        self.smallest = ""
        dfs(root, [])
        
        return self.smallest