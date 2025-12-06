class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        l, r = 1, max(nums)
        def check(mid):
            res = 0
            for num in nums:
                res += math.ceil(num/mid)
            return res <= threshold

        while l < r:
            mid = (l + r) // 2

            if check(mid) > treshold:
                r = mid
            else:
                l = mid + 1
        
        return l
        '''
        def check(mid):
            total = 0

            for num in nums:
                total += math.ceil(num/mid)
            
            return total <= threshold
        
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2

            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l