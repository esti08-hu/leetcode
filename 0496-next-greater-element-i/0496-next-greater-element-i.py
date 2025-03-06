class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n1 in nums1:
            idx = nums2.index(n1)
            found  = False 
            for i in range(idx+1, len(nums2)): 
                if nums2[i] > n1:
                    found = True
                    res.append(nums2[i])
                    break
            if not found:
                res.append(-1)
        
        return res