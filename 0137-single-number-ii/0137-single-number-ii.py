class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for k in range(32):
            tmp = 1 << k
            count1 = 0
            for num in nums:
                if num & tmp:
                    count1 += 1
            
            if count1 % 3:
                res = res | tmp
        if res & (1 << 31):
            res -= (1 << 32)
            
        return res