class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        
        for word in words:
            curr = 0
            for c in word:
                idx = ord(c) - ord("a")
                curr += weights[idx]
            res.append(chr(ord("a") + (25 - curr%26)))
        
        return "".join(res)