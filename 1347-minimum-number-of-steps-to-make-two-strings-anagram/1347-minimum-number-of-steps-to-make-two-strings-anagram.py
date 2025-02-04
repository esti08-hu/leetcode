from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        if Counter(s) == Counter(t):
            return 0
        res = 0
        for keys, values in s_count.items():
            if s_count.get(keys, 0) > t_count.get(keys, 0):
                res+=(s_count[keys] - t_count[keys])

        return res
        
