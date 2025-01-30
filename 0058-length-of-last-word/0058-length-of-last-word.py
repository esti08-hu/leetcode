class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        i=-1
        print(s[i])
        while s[i] == "":
            i-=1

        return len(s[i])