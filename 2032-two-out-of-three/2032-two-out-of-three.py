class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)
        
        nums = nums1_set.union(nums2_set)
        nums = nums.union(nums3)
        res = []
        for num in nums:
            if num in nums1_set and (num in nums2_set or num in nums3_set) or num in nums2_set and (num in nums1_set or num in nums3_set) or num in nums3_set and (num in nums1_set or num in nums2_set):
                res.append(num)
        
        return res

        