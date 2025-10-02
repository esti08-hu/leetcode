class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        memo = [[-1]*n for i in range(n)]

        def max_diff(i, j):
            if i==j:
                return nums[i]
            
            if memo[i][j]!=-1:
                return memo[i][j]
            
            diff1 = nums[i]-max_diff(i+1, j)
            diff2 = nums[j]-max_diff(i, j-1)

            res = max(diff1, diff2)

            memo[i][j] = res
            return res
        
        return max_diff(0,n-1) >= 0
