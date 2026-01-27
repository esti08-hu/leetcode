class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_cnt = Counter(s)

        res = 0
        flag = False
        for k, v in s_cnt.items():
            if not flag and v%2:
                flag = True

            if v%2:
                res += (v-1)
            else:
                res += v
        
        return res + 1 if flag else res

