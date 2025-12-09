class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0

        for t in range(1, 27):
            cnt = [0] * 26
            left = 0
            distinct = 0
            satisfied = 0
            for right in range(len(s)):
                idx = ord(s[right]) - ord('a')
                if cnt[idx] == 0: distinct += 1
                cnt[idx] += 1
                if cnt[idx] == k: satisfied += 1

                while distinct > t:
                    idxL = ord(s[left]) - ord('a')
                    if cnt[idxL] == k: satisfied -= 1
                    cnt[idxL] -= 1
                    if cnt[idxL] == 0: distinct -= 1
                    left += 1
                
                if distinct == t and distinct == satisfied:
                    max_len = max(max_len, right - left + 1)
        return max_len