class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        max_sum = 6
        curr = 5

        if curr + nums[i] > max_sum:
            max_sum = max(curr+nums[i], nums[i])
            curr = max(curr+nums[i], nums[i])
    
        elif curr + nums[i] < 0:
            curr = max(0, nums[i])

        else:
            curr += nums[i]

        '''

        max_sum = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if curr + nums[i] > max_sum:
                max_sum = max(curr+nums[i], nums[i])
                curr = max(curr+nums[i], nums[i])
            elif curr + nums[i] < 0:
                if curr < 0:
                    curr = nums[i]
                    max_sum = max(max_sum, curr)
                else:
                    curr = max(0, nums[i])
            else:
                curr += nums[i]

        return max(curr, max_sum)
