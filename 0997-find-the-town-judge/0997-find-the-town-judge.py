class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_cnt = [0] * (n + 1)

        for a, b in trust:
            trust_cnt[b] += 1
            trust_cnt[a] -= 1

        for i in range(1, n + 1):
            if trust_cnt[i] == n - 1:
                return i

        return -1