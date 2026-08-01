class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        num_idx = defaultdict(list)
        for i in range(len(nums)):
            num_idx[nums[i]].append(i)
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] in num_idx:
                        curr = num_idx[nums[i] + nums[j] + nums[k]]
                        for m in curr:
                            if m > k:
                                count += 1

        return count
