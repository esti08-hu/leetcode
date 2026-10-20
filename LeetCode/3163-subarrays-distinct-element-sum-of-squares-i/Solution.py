class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = len(nums)
        print(res)
        for i in range(len(nums) - 1):
            curr = set()
            curr.add(nums[i])
            for j in range(i+1, len(nums)):
                curr.add(nums[j])
                n = len(curr)
                res += n * n
        return res