class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ave = float("-inf")
        l = 0
        r = l + k
        curr_sum = sum(nums[l:r])

        while r <= len(nums):
            max_ave = max(max_ave, curr_sum/k)
            if r == len(nums):
                break
            curr_sum = curr_sum - nums[l] + nums[r]
            l+=1
            r+=1
            
        return max_ave

