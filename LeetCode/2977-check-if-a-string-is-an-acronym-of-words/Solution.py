class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        
        acronym = ""
        for word in words:
            acronym += word[0]
        
        return acronym == s