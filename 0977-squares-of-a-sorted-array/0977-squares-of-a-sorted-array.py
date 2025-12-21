class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        l, r = 0, n-1
        res = []
        while l <= r:
            l_sqr = nums[l] * nums[l]
            r_sqr = nums[r] * nums[r]
            if l_sqr > r_sqr:
                res.append(l_sqr)
                l+=1
            else:
                res.append(r_sqr)
                r-=1
        
        return res[::-1]
