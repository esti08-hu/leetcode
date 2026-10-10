1class Solution:
2    def earliestTime(self, tasks: List[List[int]]) -> int:
3        res = float("inf")
4        for s, e in tasks:
5            res = min(res, s + e)
6        return res