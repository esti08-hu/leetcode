class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
                
            elif char == ']':
                prev, multiplier = stack.pop()
                curr_str = prev + curr_str * multiplier

            else:
                curr_str += char

        return curr_str