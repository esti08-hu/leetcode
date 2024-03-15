class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length

        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

            
        right_product = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans