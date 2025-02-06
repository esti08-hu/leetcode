class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=0
        nums = [num for num in range(1, n+1)]
        for _ in range(n-1):
            i = (i + k - 1) % len(nums)
            nums.remove(nums[i])

        return nums[0]

