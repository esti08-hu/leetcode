from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        current_sum = 0

        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - goal]
            prefix_sums[current_sum] += 1

        return count