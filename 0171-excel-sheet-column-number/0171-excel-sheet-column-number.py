class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total = 0
        for i in range(len(columnTitle)):
            total = total * 26 + (upper.index(columnTitle[i]) + 1)
        
        return total
