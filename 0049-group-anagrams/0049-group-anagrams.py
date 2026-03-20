class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            hashMap[key].append(s)
        
        return list(hashMap.values())
