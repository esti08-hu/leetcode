class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        right = len(s)-1
        left = 0
        while left  < right:
            if s[left] != s[right]:
                count+=1
                if s[left+1] == s[right]:
                    left+=1
                elif s[left] == s[right-1]:
                    right -= 1
                else:
                    return False
            else:
                right-=1
                left+=1
                
            if count>1:
                return False
        return True  

