class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''

        max_prod = 2
        a = 2
        b = -18

        if a <= 0 or n <= 0:
            a = n
        elif a > 0:
            a *= n

        if b == 0:
            b = n
        else:
            b *= n

        max_prod = max(a, b, max_prod)

        [-2,3,3,-2,-1,-1]
        [-2,3,-1]
        [0,0,0,1,2]

        [2,-5,-2,-4,3]
         2 2  20 20 24
        '''
        a,b,max_prod = nums[0],nums[0],nums[0]

        for n in nums[1:]:
            if a <= 0 or n <= 0:
                a = n
            else:
                a *= n

            if b == 0:
                b = n
            else:
                b *= n

            max_prod = max(max_prod, a, b)

        nums = nums[::-1]

        a,b = nums[0],nums[0]
        for n in nums[1:]:
            if a <= 0 or n <= 0:
                a = n
            else:
                a *= n

            if b == 0:
                b = n
            else:
                b *= n
            
            max_prod = max(max_prod, a, b)

        return max_prod