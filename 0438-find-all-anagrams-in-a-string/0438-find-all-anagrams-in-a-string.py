from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        right = len(p)-1
        left = 0
        res = []
        print(Counter("ab")==Counter("ba"))
        while right < len(s):
            s_counter = Counter(s[left:right+1])
            if s_counter == p_counter:
                res.append(left)
            right +=1
            left +=1
            
        return res