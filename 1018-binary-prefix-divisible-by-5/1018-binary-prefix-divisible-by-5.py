class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        int_num = 0
        x = 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]:
                int_num += x
            x *= 2
        
        res = []
        x = 1
        for i in range(len(nums)-1, -1, -1):
            if not int_num % 5:
                res.append(True)
            else:
                res.append(False)
            if nums[i]:
                int_num -= x
            x *= 2
        
        return res[::-1]
