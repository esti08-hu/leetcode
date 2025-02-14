class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_value = float("inf")
        combinations = list(itertools.combinations(nums, 3))

        for comb in combinations:
            comb_sum = sum(comb)
            
            
            if abs(target - comb_sum) < abs(target - closest_value):
                closest_value = comb_sum
        return closest_value