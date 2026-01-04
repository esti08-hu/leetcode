class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        '''
        nums.sort()
        p, n, z = 0, 0, 0
        for num in nums:
            if num > 0:
                p+=1
            elif num <0:
                n += 1
            else:
                z += 1
        if n:
            i = 0
            while n and k:
                nums[i] *= -1
                i+=1
                n-=1
                k -= 1   
            if n:
                return sum(nums)   
            elif k:
                if z:
                    return sum(nums)
                else:
                    nums.sort()
                    if k%2:
                        nums[0]*=-1
                    return sum(nums)  
        '''

        nums.sort()
        p, n, z = 0, 0, 0
        for num in nums:
            if num > 0:
                p+=1
            elif num <0:
                n += 1
            else:
                z += 1
        if n:
            i = 0
            while n and k:
                nums[i] *= -1
                i+=1
                n-=1
                k -= 1
            if n:
                return sum(nums)   
            elif k:
                if z:
                    return sum(nums)
                else:
                    nums.sort()
                    if k%2:
                        nums[0]*=-1
                    return sum(nums) 
            else:
                return sum(nums) 
        elif k:
            if z:
                return sum(nums)
            else:
                nums.sort()
                if k%2:
                    nums[0]*=-1
                return sum(nums)  
        else:
            return sum(nums)
            