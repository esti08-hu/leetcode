class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        for i, c in enumerate(word):
            if c in vowels:
                res+=len(word[:i+1])*len(word[i:])
        return res