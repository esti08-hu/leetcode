class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = s[::-1]

        dp = [[0]* (len(s)+1) for _ in range(len(s) + 1)]
        max_len = [0,-1]
        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    start_in_s = i - dp[i][j]
                    start_in_t = j - dp[i][j]

                    if start_in_s == len(s) - j:
                        if dp[i][j] > max_len[0]:
                            max_len = [dp[i][j], i]
        return s[max_len[1] - max_len[0]: max_len[1]]

