class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
            n = len(nums)

            max_sum = sum(nums[:k])

            window_sum = max_sum
            
            for i in range(n - k):
                window_sum = window_sum - nums[i] + nums[i + k]
                max_sum = max(max_sum, window_sum)

            return max_sum/k