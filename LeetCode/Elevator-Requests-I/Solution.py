1class Solution:
2    def elevatorRequests(self, n: int, requests: list[int]) -> int:
3        res = requests[0]
4        prev = res
5        for r in requests[1:]:
6            res += abs(prev - r)
7            prev = r
8        return res