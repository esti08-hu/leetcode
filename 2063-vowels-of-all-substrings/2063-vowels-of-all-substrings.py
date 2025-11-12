class Solution:
    def countVowels(self, word: str) -> int:
        vouls = {"a", "e", "i", "o", "u"}
        total = 0
        n = len(word)
        for i in range(n):
            if word[i] in vouls:
                total += (i+1) * (n-i)
        
        return  total

