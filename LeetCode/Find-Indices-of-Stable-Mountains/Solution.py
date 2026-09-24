1class Solution:
2    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
3        res = []
4        for i in range(1, len(height)):
5            if height[i - 1] > threshold:
6                res.append(i)
7        return res