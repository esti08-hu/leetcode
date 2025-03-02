class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0 
        pre_dict ={0 : 1}
        count = 0

        for n in nums:
            pre += n
            pre_mod = (pre % k + k) % k 

            if pre_mod in pre_dict:
                count += pre_dict[pre_mod]
            
            pre_dict[pre_mod] = pre_dict.get(pre_mod, 0) + 1
        
        return count