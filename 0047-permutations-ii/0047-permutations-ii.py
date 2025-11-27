class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.used = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i in range(len(nums)):
                if (nums[i], i) in self.used:
                    continue

                if i > 0 and nums[i] == nums[i-1] and (nums[i-1], i-1) not in self.used:
                    continue

                self.used.add((nums[i], i))
                path.append(nums[i])
                backtrack(path)
                path.pop()
                self.used.remove((nums[i], i))
            return res

        return backtrack([])