1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for n in nums:
5            res = -1
6            for a in range(n):          
7                if (a | (a + 1)) == n:
8                    res = a
9                    break
10            ans.append(res)
11        return ans