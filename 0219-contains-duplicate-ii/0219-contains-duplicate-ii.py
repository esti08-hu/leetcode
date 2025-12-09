class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        col = set(nums[:k])
        left = 0

        for right in range(k, len(nums)):
            if nums[right] in col and abs(right - left) <= k:
                return True
            col.remove(nums[left])
            col.add(nums[right])
            left += 1
        return False
