from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        strs_dict = defaultdict(list)

        for s1 in strs:
            sorted_strs.append("".join(sorted(s1)))
        
        set_sorted_strs = set(sorted_strs)
        for s2 in strs:
            if "".join(sorted(s2)) in set_sorted_strs:
                strs_dict["".join(sorted(s2))].append(s2)
        
        return list(strs_dict.values())
