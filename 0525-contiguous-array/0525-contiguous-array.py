class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        pre = 0
        pre_dict  = {0 : -1}
        max_len = 0
        for i, n in enumerate(nums):
            if n == 0:
                pre -= 1
            else:
                pre += 1

            if pre not in  pre_dict:
                pre_dict[pre] = i

            else:
                max_len = max(max_len, i - pre_dict[pre])
        
        return max_len