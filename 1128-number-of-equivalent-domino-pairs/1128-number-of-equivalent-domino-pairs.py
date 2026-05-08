from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        
        for a, b in dominoes:
            key = (a, b) if a < b else (b, a)
            count[key] += 1
        
        total_pairs = 0
        
        for n in count.values():
            if n > 1:
                total_pairs += n * (n - 1) // 2
                
        return total_pairs