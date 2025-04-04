class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        min_pos = -1
        max_pos = -1  
        start = -1 

        for i in range(n):

            if nums[i] < minK or nums[i] > maxK:
                start = i
                min_pos = -1
                max_pos = -1

            if nums[i] == minK:
                min_pos = i

            if nums[i] == maxK:
                max_pos = i

            if min_pos != -1 and max_pos != -1:
                count += max(0, min(min_pos, max_pos) - start)

        return count