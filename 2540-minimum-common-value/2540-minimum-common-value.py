class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_nums1 = list(set(nums1))
        set_nums2 = list(set(nums2))
        # Combine elements from both lists and remove duplicates efficiently
        set_nums = (set_nums1 + set_nums2) 

        # Count the occurrences of each element
        nums_count = Counter(set_nums)

        # Filter elements with count 2 and convert to a list for printing
        val_2 = [key for key, value in nums_count.items() if value == 2]
        if val_2:
            return min(val_2)
        else:
            return -1