class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        l = len(s)
        count = 0
        for word in words:
            n = len(word)

            if n <= l and word == s[:n]:
                count += 1
        
        return count