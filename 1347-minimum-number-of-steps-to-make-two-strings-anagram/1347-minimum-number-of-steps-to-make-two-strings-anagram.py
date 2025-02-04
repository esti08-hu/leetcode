from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if Counter == Counter(t):
            return 0
            
        s_count = Counter(s)
        t_count = Counter(t)
        res = 0
        for keys, values in s_count.items():
            if s_count.get(keys, 0) > t_count.get(keys, 0):
                res+=(s_count[keys] - t_count[keys])

        return res
        
