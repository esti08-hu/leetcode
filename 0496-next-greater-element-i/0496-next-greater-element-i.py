class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        dict_s = {}
        res = []
        for n2 in nums2:
            if not stk:
                stk.append(n2)
            else:
                while stk and stk[-1] < n2:
                    x = stk.pop()
                    dict_s[x] = n2
                stk.append(n2)

        for n in nums1:
            if n not in dict_s:
                res.append(-1)
            else:
                res.append(dict_s[n])
        
        return res