class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        pre = 0
        pre_dict = {0 : -1}
        
        for i in range(len(nums)):
            pre += nums[i]
            pre_mod = pre%k
            
            if pre_mod in pre_dict:
                if i - pre_dict[pre_mod] > 1:
                    return True 
            else:
                pre_dict[pre_mod] = i

        return False
