class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        comb = []

        def backtrack(start, path):
            comb.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])

        res = 0
        for c in comb:
            curr = 0
            for num in c:
                curr^=num
            res+=curr
        return res



        