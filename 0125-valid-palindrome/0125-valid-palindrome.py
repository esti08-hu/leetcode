class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = []
        low_num = "abcdefghijklmnopqrstuvwxyz1234567890"
        up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for c in s:
            if c in low_num:
                _s.append(c)
            elif c in up:
                _s.append(low_num[up.index(c)])
        
        print(_s, s)
        return _s == _s[::-1]
