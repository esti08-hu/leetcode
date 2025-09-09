class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = []
        sorted_strs = {}
        for i, s in enumerate(strs):
            curr = list(s)
            curr.sort()
            curr = "".join(curr)
            if curr not in sorted_strs:
                sorted_strs[curr] = []
            
            sorted_strs[curr].append(s)

        return list(sorted_strs.values())



           