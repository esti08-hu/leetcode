class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)

        hash_map = {sorted_nums[0]: 0}
        x = 0

        for i in range(1, len(nums)):
            if sorted_nums[i] not in hash_map:
                x += 1
                hash_map[sorted_nums[i]] = x
            else:
                x += 1
        for i in range(len(nums)):
            res.append(hash_map[nums[i]])

        return res