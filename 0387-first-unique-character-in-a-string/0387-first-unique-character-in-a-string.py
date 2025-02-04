from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for key, val in s_count.items():
            if val == 1:
                return s.index(key)
        return -1