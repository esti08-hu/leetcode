class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            p_holer = 0
            count = 0

            for seeker in range(len(nums)):
                if seeker+1 < len(nums) and nums[seeker] == nums[seeker+1]:
                    nums[seeker] = "_"

                if nums[seeker] != "_":
                    nums[p_holer], nums[seeker] = nums[seeker], nums[p_holer]
                    p_holer += 1
                    count += 1

            return count