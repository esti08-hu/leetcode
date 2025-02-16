class Solution:
    def minimumSteps(self, s: str) -> int:
        white_count = 0
        swaps = 0
        
        for ball in s:
            if ball == '1':
                white_count += 1
            elif ball == '0':
                swaps += white_count
        
        return swaps