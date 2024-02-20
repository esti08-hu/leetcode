class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        for num in nums:
            expected_sum -= num

        return expected_sum