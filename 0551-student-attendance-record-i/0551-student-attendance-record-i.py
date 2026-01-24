class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = 0
        if s[0] == "A":
            count_A += 1
        if len(s) > 1 and s[1] == "A":
            count_A += 1
        if count_A == 2:
            return False

        for i in range(2, len(s)):
            if s[i-2] == s[i-1] == s[i] and s[i] == "L":
                return False
            if s[i] == "A":
                count_A += 1
            if count_A == 2:
                return False 
        return True