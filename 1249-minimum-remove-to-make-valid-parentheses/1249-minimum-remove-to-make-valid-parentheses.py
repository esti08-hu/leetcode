class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_indices = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove_indices.add(i)
        
        remove_indices.update(stack)
        
        result = [char for i, char in enumerate(s) if i not in remove_indices]
        
        return ''.join(result)