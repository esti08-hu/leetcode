class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:
            set_word_lower = set(word.lower())
            if any(set_word_lower.issubset(row) for row in rows):
                res.append(word)
        
        return res