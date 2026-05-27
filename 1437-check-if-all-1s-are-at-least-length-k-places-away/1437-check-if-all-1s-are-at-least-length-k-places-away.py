class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if idx == -1 and nums[i] == 1:
                idx = i

            elif idx != -1 and nums[i] == 1:
                if i - idx < k+1:
                    return False
                else:
                    idx = i
            print(idx)
        return True
