class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = [float("-inf"), float("inf")]

        for num in nums:
            if num < 0:
                res[0] = max(res[0], num)
            else:
                res[1] = min(res[1], num)
        
        if 0 - res[0] < res[1]:
            return res[0]
        else:
            return res[1]
