class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0] > nums[1] or len(nums) <= 3:
            return False    
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                break
            if nums[i] == nums[i-1]:
                return False
        print(nums[:i])
        
        if len(nums[:i]) <= 1:
            return False
        i -= 1

        for j in range(i+1, n):
            if nums[j] > nums[j-1]:
                break
            if nums[j] == nums[j-1]:
                return False
        print(nums[i:j])

        if len(nums[i:j]) <= 1:
            return False

        for k in range(j, n):
            if nums[k] < nums[k-1]:
                return False
            if nums[k] == nums[k-1]:
                return False
        print(nums[j:])
        j-=1
        
        if len(nums[j:]) <= 1:
            return False
        
        return True


