class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s+=s
        return goal in s