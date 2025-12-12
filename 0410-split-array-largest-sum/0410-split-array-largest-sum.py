class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
        32 - 7 
        7 9 14 24 32
        7 32 - 7 25
        7 32 - 9 23
        14 32-14 18
        24 32 - 24

        left, right = 0, sum(nums)=>32
        '''

        def check(mid):
            count = 1
            curr = 0
            for i in range(len(nums)):
                curr += nums[i]
                if curr > mid:
                    count += 1
                    curr = nums[i]

            return count

        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left
