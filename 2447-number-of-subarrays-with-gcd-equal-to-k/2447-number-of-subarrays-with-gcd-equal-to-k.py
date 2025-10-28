class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i]%k!=0:
                continue
            for j in range(i+1, n+1):
                if gcd(*(n for n in nums[i:j])) == k:
                    count +=1
                else:
                    continue
        
        return count