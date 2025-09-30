class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> list:
        def dfs(i, curr):
            if i == len(s):
                return [" ".join(curr)]

            res = []
            for word in wordDict:
                if s.startswith(word, i):
                    res += dfs(i + len(word), curr + [word])
            return res

        return dfs(0, [])