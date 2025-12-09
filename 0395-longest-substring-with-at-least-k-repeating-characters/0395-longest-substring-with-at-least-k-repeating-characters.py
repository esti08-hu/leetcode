class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(l, r):
            if r - l < k:
                return 0
            
            freq = [0] * 26
            for i in range(l, r):
                freq[ord(s[i]) - ord('a')] += 1
            
            split_char = None

            for i in range(26):
                if 0 < freq[i] < k:
                    split_char = chr(i + ord('a'))
                    break
            
            if split_char is None:
                return r - l
            
            max_len = 0
            start = l
            for i in range(l, r):
                if s[i] == split_char:
                    max_len = max(max_len, dfs(start, i))
                    start = i+1
            max_len = max(max_len, dfs(start, r))
            return max_len
        return dfs(0, len(s))