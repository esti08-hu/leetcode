class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count = 1
        acc = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if acc + widths[idx] > 100:
                acc = 0 
                count += 1
            acc += widths[idx]
        
        return [count, acc]

