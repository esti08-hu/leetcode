class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    print(curr)
                    backtrack(curr)
                    curr.pop()

        res = []
        backtrack([])
        return res