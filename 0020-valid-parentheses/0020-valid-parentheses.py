class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"(":")", "[":"]", "{":"}"}
        stk = []

        for i in range(len(s)):
            if s[i] not in hashMap:
                if not stk or hashMap[stk.pop()] != s[i]:
                    return False
            else:
                stk.append(s[i])
        
        return not stk